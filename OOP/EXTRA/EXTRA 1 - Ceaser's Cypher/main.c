#include <stdio.h>


// function that read the file with 26 lines and store it in an array
void read_distribution(char *filename, float *arr) {
    FILE *fp;                        // File pointer
    fp = fopen(filename, "r");       // Open a file in read mode
    for(int i = 0; i < 26; i++) {
        fscanf_s(fp, "%f", &arr[i]); // Read the content and store it inside array
    }
    fclose(fp);                      // Close the file
}


// function that computes the frequency of each letter in file
void compute_frequency(char *filename, float *arr) {

    FILE *fp;
    fp = fopen(filename, "r");
    char ch;
    int count = 0;
    while((ch = (char)fgetc(fp)) != EOF) {
        if(ch >= 'a' && ch <= 'z') {
            arr[ch - 'a']++;
            count++;
        }
        if(ch >= 'A' && ch <= 'Z') {
            arr[ch - 'A']++;
            count++;
        }
    }
    for(int i = 0; i < 26; i++) {
        arr[i] = arr[i] / (float)count;
    }
    fclose(fp);
}


// function that computes the chi-square value
float chi_square(const float *dist, const float *encr) {
    float chi_square = 0;
    for(int i = 0; i < 26; i++) {
        chi_square += (encr[i] - dist[i]) * (encr[i] - dist[i]) / dist[i];
    }
    return chi_square;
}


// shift array to the right
void shift_array(float *arr) {
    float temp = arr[25];
    for(int i = 25; i > 0; i--) {
        arr[i] = arr[i - 1];
    }
    arr[0] = temp;
}


// for every shift, compute the chi-square value and store the minimum value
void compute_shift(float *dist, float *encr, int *countSteps) {
    float min_chi_square = chi_square(dist, encr);
    for(int i = 1; i < 26; i++) {
        shift_array(encr);
        float temp = chi_square(dist, encr);
        if(temp < min_chi_square) {
            *countSteps = i;
            min_chi_square = temp;
        }
    }
}


// print the decrypted text
void print_decrypted_text(char *filename, int countSteps) {
    printf("The decrypted text is: \n");
    FILE *fp;
    fp = fopen(filename, "r");
    char ch;
    while((ch = (char)fgetc(fp)) != EOF) {
        if(ch >= 'a' && ch <= 'z') {
            printf("%c", (char)((int)(ch - 'a' + countSteps)%26 + 'a'));
        }
        else {
            if(ch >= 'A' && ch <= 'Z') {
                printf("%c", (char)((int)(ch - 'A' + countSteps)%26 + 'A'));
            }
            else {
                printf("%c", ch);
            }
        }
    }
    fclose(fp);
}


int main() {

    float dist[26];
    read_distribution("distribution.txt", dist);

    float encr[26] = {0};
    compute_frequency("in.txt", encr);

    int countSteps = 0;
    compute_shift(dist, encr, &countSteps);

    printf("The number of steps is: %d\n", countSteps);

    print_decrypted_text("in.txt", countSteps);

    return 0;
}

