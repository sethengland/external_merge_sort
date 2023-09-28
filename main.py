from write import write_integers
from sort import read_and_sort
from verify import verify_is_sorted
from helpers import tear_down_previous

if __name__ == "__main__":
    to_sort_filename = "generated_out.bin"
    sorted_filename = "final_sorted.bin"
    tear_down_previous(to_sort_filename, sorted_filename)
    print("tear down successful")
    N = 100000 #total number of integers
    M = 1000   #maximum integers allowed to read into memory
    write_integers(to_sort_filename, N)
    print("write stage complete")
    read_and_sort(to_sort_filename, sorted_filename, M)
    print("sort complete")
    if verify_is_sorted(sorted_filename, M):
        print("success")
    else:
        print("sorted verification failed")
