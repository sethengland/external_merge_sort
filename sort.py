import heapq
import struct


def read_and_sort(input, sorted_filename, M):
    in_file = open(input, 'rb')
    chunk_names = []
    chunk_number = 0
    while True:
        chunk = in_file.read(M * 4)
        if len(chunk) == 0:
            break
        data = list(struct.unpack('I' * (len(chunk) // 4), chunk))
        data.sort()
        output = "out_" + str(chunk_number) + ".bin"
        out_file = open(output, 'wb')
        prev = data[0]
        for num in data:
            if num < prev:
                print("NOT SORTED")
            prev = num
            out_file.write(struct.pack('I', num))
        out_file.close()
        chunk_number += 1
        chunk_names.append(output)
    in_file.close()
    k_way_merge_chunks(chunk_names, sorted_filename)

    
def k_way_merge_chunks(chunk_names, sorted_filename):
    final_out = open(sorted_filename, 'wb')
    K = len(chunk_names)
    heap = []
    reading_buffers = []
    for i in range(K):
        reading_buffers.append(open(chunk_names[i], 'rb'))
        first_element_data = struct.unpack('I', reading_buffers[i].read(4))[0]
        heapq.heappush(heap, (first_element_data, i))
    while len(heap) > 0:
        ele, idx = heapq.heappop(heap)
        final_out.write(struct.pack('I', ele))
        rw = reading_buffers[idx].read(4)
        if len(rw) != 4:
            continue
        next_element_data = struct.unpack('I', rw)[0]
        heapq.heappush(heap, (next_element_data, idx))
    
    final_out.close()
    for f in reading_buffers:
        f.close()
    
