# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 09:59:41 2019
@author: Leon
内容：
人脸验证准确率测试
样本：LFW人脸集，共6000对人脸，中3000对同一身份、3000对不同身份。
"""
import numpy as np
import cv2
import tensorflow as tf
import matplotlib.pyplot as plt
# facenet 和 detect_face 均在facenet项目文件中，这里是直接将其放到测试脚本同一路径下了，也可以安装facenet,然后调用之
import facenet.src.facenet as facenet
import facenet.src.align.detect_face as detect_face


def face_verification(img_pairs_list):
    model = r'facenet\src\align'
    model_facenet = './20170512-110547.pb'
    # mtcnn相关参数
    minsize = 40
    threshold = [0.4, 0.5, 0.6]  # pnet、rnet、onet三个网络输出人脸的阈值，大于阈值则保留，小于阈值则丢弃
    factor = 0.709  # scale factor

    # 创建mtcnn网络
    with tf.Graph().as_default():
        sess = tf.compat.v1.Session()
        with sess.as_default():
            pnet, rnet, onet = detect_face.create_mtcnn(sess, model)

    margin = 44
    image_size = 160

    with tf.Graph().as_default():

        with tf.compat.v1.Session() as sess:

            # 根据模型文件载入模型
            facenet.load_model(model_facenet)
            # 得到输入、输出等张量
            images_placeholder = tf.compat.v1.get_default_graph().get_tensor_by_name("input:0")
            embeddings = tf.compat.v1.get_default_graph().get_tensor_by_name("embeddings:0")
            phase_train_placeholder = tf.compat.v1.get_default_graph().get_tensor_by_name("phase_train:0")

            # 设置可视化进度条相关参数
            jd = '\r   %2d%%\t [%s%s]'
            bar_num_total = 50
            total_num = len(img_pairs_list)
            result, dist = [], []

            for i in range(len(img_pairs_list)):

                # 画进度条
                if i % (total_num / bar_num_total) == 0 or i == total_num - 1:
                    bar_num_alright = round(bar_num_total * i / total_num)
                    alright = '#' * bar_num_alright
                    not_alright = '□' * (bar_num_total - bar_num_alright)
                    percent = (bar_num_alright / bar_num_total) * 100
                    print(jd % (percent, alright, not_alright), end='')

                # 读取一对人脸图像
                img_pairs = img_pairs_list[i]
                img_list = []
                img1 = cv2.imread(img_pairs[0])
                img2 = cv2.imread(img_pairs[1])

                img_size1 = np.asarray(img1.shape)[0:2]
                img_size2 = np.asarray(img2.shape)[0:2]

                # 检测该对图像中的人脸
                bounding_box1, _1 = detect_face.detect_face(img1, minsize, pnet, rnet, onet, threshold, factor)
                bounding_box2, _2 = detect_face.detect_face(img2, minsize, pnet, rnet, onet, threshold, factor)

                # 未检测到人脸，则将结果标为-1，后续计算准确率时排除
                if len(bounding_box1) < 1 or len(bounding_box2) < 1:
                    result.append(-1)
                    dist.append(-1)
                    continue

                # 将图片1加入img_list
                det = np.squeeze(bounding_box1[0, 0:4])
                bb = np.zeros(4, dtype=np.int32)
                bb[0] = np.maximum(det[0] - margin / 2, 0)
                bb[1] = np.maximum(det[1] - margin / 2, 0)
                bb[2] = np.minimum(det[2] + margin / 2, img_size1[1])
                bb[3] = np.minimum(det[3] + margin / 2, img_size1[0])
                cropped = img1[bb[1]:bb[3], bb[0]:bb[2], :]
                aligned = cv2.resize(cropped, (image_size, image_size))
                prewhitened = facenet.prewhiten(aligned)
                img_list.append(prewhitened)

                # 将图片2加入img_list
                det = np.squeeze(bounding_box2[0, 0:4])
                bb = np.zeros(4, dtype=np.int32)
                bb[0] = np.maximum(det[0] - margin / 2, 0)
                bb[1] = np.maximum(det[1] - margin / 2, 0)
                bb[2] = np.minimum(det[2] + margin / 2, img_size2[1])
                bb[3] = np.minimum(det[3] + margin / 2, img_size2[0])
                cropped = img2[bb[1]:bb[3], bb[0]:bb[2], :]
                aligned = cv2.resize(cropped, (image_size, image_size))
                prewhitened = facenet.prewhiten(aligned)
                img_list.append(prewhitened)

                images = np.stack(img_list)

                # 将两个人脸转化为512维的向量
                feed_dict = {images_placeholder: images, phase_train_placeholder: False}
                emb = sess.run(embeddings, feed_dict=feed_dict)

                # 计算两个人脸向量的距离
                ed = np.sqrt(np.sum(np.square(np.subtract(emb[0], emb[1]))))
                dist.append(ed)
                # 根据得出的人脸间的距离，判断是否属于同一个人
                if ed <= 1.1:
                    result.append(1)
                else:
                    result.append(0)
    return result, dist


def get_img_pairs_list(pairs_txt_path, img_path):
    """ 指定图片组合及其所在文件，返回各图片对的绝对路径
        Args:
            pairs_txt_path：图片pairs文件，里面是6000对图片名字的组合
            img_path：图片所在文件夹
        return:
            img_pairs_list：深度为2的list，每一个二级list存放的是一对图片的绝对路径
    """
    file = open(pairs_txt_path)
    img_pairs_list, labels = [], []
    while 1:
        img_pairs = []
        line = file.readline().replace('\n', '')
        if line == '':
            break
        line_list = line.split('\t')
        if len(line_list) == 3:
            # 图片路径示例：
            # 'C:\Users\thinkpad1\Desktop\image_set\lfw_funneled\Tina_Fey\Tina_Fey_0001.jpg'
            img_pairs.append(
                img_path + '\\' + line_list[0] + '\\' + line_list[0] + '_' + ('000' + line_list[1])[-4:] + '.jpg')
            img_pairs.append(
                img_path + '\\' + line_list[0] + '\\' + line_list[0] + '_' + ('000' + line_list[2])[-4:] + '.jpg')
            labels.append(1)
        elif len(line_list) == 4:
            img_pairs.append(
                img_path + '\\' + line_list[0] + '\\' + line_list[0] + '_' + ('000' + line_list[1])[-4:] + '.jpg')
            img_pairs.append(
                img_path + '\\' + line_list[2] + '\\' + line_list[2] + '_' + ('000' + line_list[3])[-4:] + '.jpg')
            labels.append(0)
        else:
            continue

        img_pairs_list.append(img_pairs)
    return img_pairs_list, labels


def roc(dist, labels):
    TP_list, TN_list, FP_list, FN_list, TPR, FPR = [], [], [], [], [], []
    for t in range(180):
        threh = 0.1 + t * 0.01

        TP, TN, FP, FN = 0, 0, 0, 0
        for i in range(len(dist)):
            if labels[i] == 1 and dist[i] != -1:
                if dist[i] < threh:
                    TP += 1
                else:
                    FN += 1
            elif labels[i] == 0 and dist[i] != -1:
                if dist[i] >= threh:
                    TN += 1
                else:
                    FP += 1
        TP_list.append(TP)
        TN_list.append(TN)
        FP_list.append(FP)
        FN_list.append(FN)
        TPR.append(TP / (TP + FN)) # 灵敏度/召回率。表示所有正例中，被分对的比例，衡量给了分类器对正例的识别能力。
        FPR.append(FP / (FP + TN)) # 负样本识别错误总数 / 负例总数
        
    return TP_list, TN_list, FP_list, FN_list, TPR, FPR


if __name__ == '__main__':
    pairs_txt_path = './pairs.txt'
    img_path = './dataset/lfw'
    img_pairs_list, labels = get_img_pairs_list(pairs_txt_path, img_path)

    result, dist = face_verification(img_pairs_list)

    num_right, num_total = 0, 0
    num_total = len([r for r in result if r != -1])
    num_right = len([result[i] for i in range(len(result)) if result[i] == labels[i]])

    print("人脸验证测试完毕")
    print("阈值为1.1，共%d对人脸，准确率%2.4f%%" % (num_total, round(100 * num_right / num_total, 4)))

    TP_list, TN_list, FP_list, FN_list, TPR, FPR = roc(dist, labels)
    fig, (ax1,ax2) = plt.subplots(1,2,sharey = True)
    ax1.plot(FPR, TPR, label='Roc')
    ax1.plot([0, 1], [0, 1], '--', color=(0.6, 0.6, 0.6), label='Luck')
    ax1.set_xlabel('FPR')
    ax1.set_ylabel('TPR')
    ax1.legend()

    ax2.plot(np.linspace(0.1, 1.89, 180), TP_list, label='TP')
    ax2.plot(np.linspace(0.1, 1.89, 180), TN_list, label='TN')
    ax2.plot(np.linspace(0.1, 1.89, 180), FP_list, label='FP')
    ax2.plot(np.linspace(0.1, 1.89, 180), FN_list, label='FN')
    ax2.legend()
    fig.show()