# generator function to read each line for the input file
def genread(fname):
  with open (fname) as f:
    l = f.readlines()
    for line in l:
      yield line.strip('\r\n')

def max_share_price():
  global company_dictionary
  itr = genread(filename)
  # iterating only the first row to create keys of the output dictionary
  for idx,i in enumerate(itr):
    if idx==0:
      for comp_name in i.split(',')[2:]:
        company_dictionary.update({comp_name:['']*2 + [0,]})
    break

  # iterating rest of the rows to find the maximum share price for each company
  for idx,row in enumerate(itr):
    data = row.split(',')
    year = data[0]
    month= data[1]
    for d_idx, company in enumerate(sorted(company_dictionary.keys())):
      try:
        if company_dictionary[company][2] < int(data[d_idx+2].strip(' ')):
          company_dictionary.update({company:[year, month, int(data[d_idx+2])]})
      except Exception, e:
        ## Exception in case the data in input file is not proper
        print "ERROR: %s" % (e,)
        exit(1)
  return company_dictionary
 
### unit test
import unittest
class max_share_price_unit_test(unittest.TestCase):
    def setUp(self):
      # the expected result i as follows
      self.max_share_price_dict = {'Company D': ['2000', ' May', 56], 'Company A': ['2011', ' Jun', 150], 'Company B': ['2012', ' Aug', 16], 'Company C': ['1990', ' Jan', 201]}

    def test_max_share_price(self):
      self.assertEqual(max_share_price(), self.max_share_price_dict, 'the output for calculating maximum share price is wrong')

if __name__ == "__main__":
  filename='input.txt'
  company_dictionary={}
  print max_share_price()
  unittest.main()
  
