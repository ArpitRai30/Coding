// multiplication of two matrix


#include <stdio.h>
void main() {
    int m, n, p, q, i, j, k, sum;
    printf("Enter the row and column sizes of matrix-1 : ");
    scanf("%d %d", &m, &n);
    printf("\nEnter the row and column sizes of matrix-2 : ");
    scanf("%d %d", &p, &q);
    int mat1[m][n];
    int mat2[p][q];
    int res[m][q];

    for(i=0; i<m; i++){
        for(j=0; j<q; j++){
            res[i][j]=0;
        }
    }
    printf("Enter matrix-1 six elements : ");
    for(i=0; i<m; i++){
        for(j=0; j<n; j++){
            scanf("%d", &mat1[i][j]);
        }
    }

    printf("Enter matrix-2 six elements : ");
    for(i=0; i<p; i++){
        for(j=0; j<q; j++){
            scanf("%d", &mat2[i][j]);
        }
    }

    printf("The given matrix-1 is\n");
    for(i=0; i<m; i++){
        for(j=0; j<n; j++){
            printf("%d ", mat1[i][j]);
        }
        printf("\n");
    }

    printf("The given matrix-2 is\n");
    for(i=0; i<p; i++){
        for(j=0; j<q; j++){
            printf("%d ", mat2[i][j]);
        }
        printf("\n");
    }

    if(n==p){
        printf("Multiplication of two matrices is\n");
        for(i=0; i<m; i++){
            for(j=0; j<q; j++){
                for(k=0; k<n; k++){
                    res[i][j] = res[i][j] + (mat1[i][k] * mat2[k][j]);
                }
            }
        }
        for(i=0; i<m; i++){
            for(j=0; j<q; j++){
                printf("%d ", res[i][j]);
            }
            printf("\n");
        }
    }

    else{
        printf("Multiplication is not valid");
    }
}