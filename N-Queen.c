#include<stdio.h>

// using namespace std;

int n;

int check(int a[n][n], int i, int j)
{
      for (int col = j;col>=0; col --)
      {
            if (a[i][col] == 1)
                  return 0;
      }
      for (int row=i,col=j; row<n;row++,col--)
      {
            if (a[row][col] == 1)
                  return 0;
      }

      for(int row=i,col=j;row>=0;row--,col--)
      {
            if(a[row][col] == 1)
                  return 0;
      }
      return 1;
}

int queen(int a[n][n], int j)
{
      if (j == n)
            return 1;
      else
      {
            for(int i=0;i<n;i++)
            {
                  if (check(a,i,j))
                  {
                        a[i][j] = 1;
                        if (queen(a,j+1))
                        {
                              return 1;
                        }
                        a[i][j] = 0;
                  }
            }
            return 0;
      }
}

int main()
{
      scanf("%d", &n);
      int a[n][n];
      for (int i = 0; i<n*n;i++)
            a[0][i] = 0;
      if (queen(a,0))
      {
            for(int i = 0; i<n*n;i++)
            {
                  printf("%d ",a[0][i]);
                  if((i+1)%n== 0)
                        printf("\n");
            }
      }
      return 0;
}


