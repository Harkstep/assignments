import sys, glob, os

# Get the directory name
if sys.platform == 'win32':
    hdir = os.environ['HOMEPATH']
else:
    hdir = os.environ['HOME']

# Construct a portable wildcard pattern
pattern = os.path.join(hdir,'*')                         # This sets pattern as incoming files variable.?
# use os.path.getsize() to find each files size          # This calls the file size
# using os.path.basename()                               # This calls the end file in the path("basename").
# Use glob.glob() to obtain list of filenames            # This calls the files obtained by pattern?



# #TODO: Use the glob.glob() function to obtain the list of filenames
# print('#TODO: Use the glob.glob() function to obtain the list of filenames')
#
# print(glob.glob(pattern))                           # simply prints filenames
#
# print('')
# print('')
#
#
# # TODO: use os.path.getsize to find each file's size
# print('# TODO: use os.path.getsize to find each file"s size')
#
# file_list = glob.glob(pattern)                    # sets file_list variable for pattern files
# for file in file_list:                            # this grabs each file in file_list for entire list
#     print(file, os.path.getsize(file))            # this prints the file name, followed by the file size
#
# print('')
# print('')
#
#
#
# # TODO: Add a test to only display files that are not zero length
# print('# TODO: Add a test to only display files that are not zero length')
#
# file_list = glob.glob(pattern)
# for file in file_list:
#     if os.path.getsize(file) > 0:                      # this if statement places a conditional that file size must
#         print(file, os.path.getsize(file))             # be greater than 0 for it to print
#
# print('')
# print('')
#
#
# # TODO: Remove the leading directory name(s) from each filename before you print it -
# print('# TODO: Remove the leading directory name(s) from each filename before you print it -')

# print('')
# print('')
#
# file_list = glob.glob(pattern)                                    # This simply repeats the code above but this
# for file in file_list:                                            #time adding in the new .basename command.
#         print(os.path.basename(file), os.path.getsize(file))
#

print('')
print('')

print('All TODOs combined')                             # with exception of printing glob.glob file first
print('')                                               # This combined code covers all the above TODOs
file_list = glob.glob(pattern)                          # This obviously still relies on the files built in to the
for file in file_list:                                  # exercise at top of page.
    if os.path.getsize(file) > 0:
        print(os.path.basename(file), os.path.getsize(file))