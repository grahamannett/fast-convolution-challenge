# Assignment - Matic Coding Challenge

**Objective: Develop a program using a production language (e.g., Rust, C, C++, Python, or Swift, excluding languages like Matlab, JavaScript, or Java) that performs the following tasks:**

Read integer arguments 'rows' and 'columns (cols)' from the command line.

Create an unsigned char matrix M of size [rows x cols]

Populate M with random non-negative integers covering the range of the data type.

Convolve the matrix M with a constant filter K=[-1, 0, 1] along both the rows & cols axis (i.e. along the vertical & horizontal axis respectively). Correlation and convolution differ by a sign, so compute either.

The code MUST be optimized primarily for speed (fast execution) and efficiency (in terms of memory). We will also assess for simplicity and cleanliness of the code.

We will NOT be assessing the solution for generalization ability.

Filter K is constant and it doesn't change for this problem.

Post-filter matrices Dx and Dy must be mathematically accurate.

Gracefully handle border conditions as per your preferences and note assumptions in code comments.

The solution should only be developed for a single-core CPU, without using GPUs or multiprocessing.

Save vertical and horizontal convolution results in two output matrices Dy and Dx respectively.

Display computation times for both Dx and Dy.

Determine and print the min and max values of Dx and Dy separately.

## Requirements/Notes:

If writing in Rust/C/C++/Swift:

Provide compile flags in the code comments.

Please don't use an extra library if writing in these languages.

If writing in C/C++, must follow C/C++17 or later standards.

If writing in Python:

Optimize code for maximum speed.

Submission of Jupyter Notebooks or something similar will be auto-rejected.

Feel free to use Numpy library if suitable. The solution would still be evaluated for maximum speed.

Problem-solving skills in unfamiliar, ambiguous scenarios will be assessed. Thus only submit your preferred solution.

For the definition of convolution, feel free to search the internet.

# Submission Instructions:

1. Once complete, please submit your coding file directly through this submission form.
2. Please include the code file only (no zip/tar of the code, no cache files and no commit files). Please attach files directly without packing them in a zip.
3. Please only send one source file unless it’s absolutely not possible to put the code in one file, e.g. attaching Makefiles.
4. Please write/include your assumptions as comments in the source code file only. No separate preparation for this challenge.
5. Please make this challenge or its response public on your GitHub.