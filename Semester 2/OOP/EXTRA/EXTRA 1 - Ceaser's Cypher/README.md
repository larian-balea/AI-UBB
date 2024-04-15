# Frequency Analysis Decryption

This C program aims to perform decryption using frequency analysis. It reads the distribution of letters from a file, computes the frequency of each letter in the encrypted text, calculates the chi-square value for each possible shift, and prints the decrypted text.

## Features

- **Read Distribution**: Reads the distribution of letters from a file containing 26 lines, each representing the frequency of a letter in the English alphabet.

- **Compute Frequency**: Computes the frequency of each letter in the encrypted text from another file.

- **Compute Chi-Square Value**: Computes the chi-square value for the frequency distribution of the encrypted text compared to the known distribution.

- **Shift Array**: Provides a function to shift an array to the right by one position.

- **Compute Shift**: For every shift, computes the chi-square value and stores the minimum value, indicating the number of steps required to decrypt the text.

- **Print Decrypted Text**: Prints the decrypted text by applying the appropriate shift to each letter.

## Usage

1. **Input Files**:
   - Create a file named `distribution.txt` containing 26 lines, each representing the frequency of a letter in the English alphabet.
   - Create an encrypted text file, e.g., `in.txt`, containing the text to be decrypted.

2. **Compilation**:
   - Compile the program using a C compiler:
     ```bash
     gcc -o decryption decryption.c
     ```

3. **Execution**:
   - Run the compiled program and provide the input files as arguments:
     ```bash
     ./decryption
     ```

4. **Output**:
   - The program will output the number of steps required for decryption and print the decrypted text.

## File Structure

- `decryption.c`: The main C source code file containing all functions for frequency analysis decryption.
- `distribution.txt`: Input file containing the distribution of letters in the English alphabet.
- `in.txt`: Input file containing the encrypted text to be decrypted.

## Dependencies

- This program does not depend on any external libraries.

## Contributors

- **Balea Larian**: larian.balea@gmail.com
