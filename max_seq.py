# given a list of integers L, find the maximum 
# length of a sequence of consecutive numbers that 
# can be formed using elements from L 
# [5, 2, 99, 3, 4, 1, 100] -> max(|{99, 100}|, |{1 , 2, 3, 4, 5}|) = 5

# runtime is O(nlog(n)) 
# space complexity is O(1)
def sort_seq(seq):
   # sort function is Timesort -> nlog(n) run time
   seq.sort()

   length = 0
   max_length = 0
   l = len(seq)

   # iterate through ordered list
   for i in range(l-1):

      # chechk current index and next index
      if seq[i] == seq[i+1] - 1:
         length += 1
         
      else:
         # adds last element if next element isn't in list
         if i > 0 and seq[i] - 1 == seq[i-1]:
            length += 1

         # stores longest sequence
         max_length = max(length, max_length)
         length = 0

   return max_length


# runtime is O(n)
# space complexity is O(n)
def max_seq(seq):

   # list keeps track of numbers in a previous sequence
   visits = [False] * len(seq)

   # need to convert list to set for O(1) lookup time
   # lookup time for list is O(n)
   seq_set = set(seq)
   count = 0
   max_count = 0

   for i in range(len(visits)):
      # check that index hasn't been visited
      if not visits[i]:
         visits[i] = True
         count += 1

         # search for numbers before and after
         next_int = seq[i] + 1
         prev_int = seq[i] - 1

         while next_int in seq_set:
            count += 1
            next_int += 1

         while prev_int in seq_set:
            count += 1
            prev_int -= 1

      # keep longest count
      max_count = max(count, max_count)
      count = 0


   return max_count

def main():
   seq = [5, 2, 99, 3, 4, 1, 100]

   sort = sort_seq(seq)
   no_sort = max_seq(seq)
   
   print(sort)
   print(no_sort)

   return

if __name__ == '__main__':
   main()