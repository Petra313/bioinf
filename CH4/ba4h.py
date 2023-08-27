
def GenerateConvolutionSpectrum(spectrum):
  output = [] # subtraction vaue
  for i in spectrum: # row val
    for j in spectrum: # col val
      if (i-j) > 0:
        output.append(i-j) 
  
  # counting frequency
  freq = {}
  for item in output:
    if item in freq:
      freq[item] += 1
    else:
      freq[item] = 1
  
  # s
  sorted_list = [k for k, j in sorted(freq.items(), key=lambda item: item[1], reverse=True)] #sorts by count and returns key
  
  # multiplying with frequency 
  ans = []
  for item in sorted_list:
      ans += [item] * freq[item]
  return ans

# main function
with open('rosalind_ba4h.txt', 'r') as f:
  for line in f:  #Line is a string, split the string on whitespace
    numbers_str = line.split()
    #convert numbers to int
    spectrum = [int(x) for x in numbers_str] 

result = GenerateConvolutionSpectrum(spectrum)
for res in result:
  print(res, end=' ')
