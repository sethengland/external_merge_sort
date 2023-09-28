# I run this program directly in my IDE and I configure the N and M variables directly in the main function, though making them command line arguments would be a nice ease of use addition.

## random notes
* I run cleanup before the next run rather than after the current run so you can
see all the files including intermediary and final result files. The final result is
`final_sorted.bin` while the random unsorted file is `generated_out.bin`. All the
chunked files are called `out_{index}.bin`.
* Requiring more than 10,000 chunks (N // M) seems to be somewhat of an upper
bound as either Python or my RAM does not like it and it crashes because I have
opened too many files.
* I ran this with N = billion and M = million and it took quite a while but 
it didn't crash and the sort verification passed.

## I'll prepare to talk about this more in the interview but regarding the follow up questions:
* I don't have much experience multithreading/parallelism in Python so that's
why I didn't implement any in this program but basically yes this program is
IO bound, and an straightforward way to add parallelism would be to immediately
continue reading the next chunk and then sort as that chunk is being read.
* All the sorting can be done independently (across cores/disks/machines),
the merging just has to be done on the same machine to get the final result.