# Suduko-solving-program

Suduko is a 9 x 9 grid containing numbers from 0-9 which requires that no number be repeated in a row, column and the smaller 3 x 3 grids.

The input taken is an incomplete suduko which then the algorithm completes.

The input is taken in the form of 9 lists with contain the 9 rows of the incomplete suduko. This is then converted into a numpy array using the numpy library. A copy of this array is made- over which the nesseccary functions will work on- and its size is set.

The first step to solve a suduko is to figure out all possible numbers that can be put in an empty box in the grid that are not repeated in the respective row, column or 3 x 3 grid of the box.

This step is taken care of by function 'probable_numbers'.

After this, we get many element positions with only one possible number. This forms the basis of further sorting.

Further sorting uses one basic principle that any single element in the grid is at its permanent position and it cannot be repeated anywhere in its respective row, column or 3 x 3 grid.

The functions 'row', 'column' and 'box' make sure that no number is repeated in a row, column and 3 x 3 grid respectively.

These three functions executing in a loop complete the suduko where every element is at its permanent position. 
