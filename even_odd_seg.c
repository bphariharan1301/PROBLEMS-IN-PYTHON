#include <stdio.h>

int main()
{
  int n, ind, safe, shift, e_ind;
  scanf("%d", &n);
  int arr[n];
  for (ind = 0; ind < n; ind++)
  {
    scanf("%d", &arr[ind]);
  }

  for (ind = 0; ind < n; ind++)
  {
    while (arr[ind] % 2 == 0)
    {
      ind++;
    }
    for (e_ind = ind + 1; e_ind < n && arr[e_ind] % 2 != 0; e_ind++)
    {
      if (e_ind >= n)
        break;
      safe = arr[e_ind];

      for (shift = e_ind; shift > ind; ind--)
      {
        arr[shift] = arr[shift - 1];
      }
      arr[ind] = safe;
    }
  }

  for (ind = 0; ind < n; ind++)
    printf("%d", arr[ind]);

  return 0;
}