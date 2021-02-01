~~~c

# include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include "cv.h"
#include "highgui.h"
 
#pragma comment(lib, "cv.lib")  
#pragma comment(lib, "cxcore.lib")  
#pragma comment(lib, "highgui.lib") 
 
int main()
{
  int length,width,step,channel;
  uchar * data;
  int i,j,k;
  IplImage* img;
  img=cvLoadImage("1.jpg",0);
 
  cvNamedWindow("source",0);
  cvShowImage("source",img);
 
  if(!img)
  printf("could not find the image\n");
  length=img->height;
  width=img->width;
  step=img->widthStep;
  channel=img->nChannels;  
  data=(uchar*)img->imageData;
  for(i=0;i<=length-1;i++)
	{
		 for(j=0;j<=width-1;j++)
		 {
			  for(k=0;k<=channel-1;k++)
			  {
			   data[i*step+j*channel+k]=255-data[i*step+j*channel+k];
			  }
		 }
	}
  cvNamedWindow("convert",0);
  cvShowImage("convert",img);
  cvWaitKey(0);
  cvReleaseImage(&img);
  return 0;
}
~~~

图像反转：灰度图像范围为[0,L-1]的图像反转，表达式s=L-1-r；用这种方式倒转图像的强度，可产生图像反转的对等图像。