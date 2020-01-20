import os, sys, time

# global variables
_cached_last_time_files = {} # save last modification date for each file
_deleted_files = []
cached_files_dir = "cache"

def save_in_cache(file_path):
    if os.path.splitext(os.path.basename(file_path))[1]!='.txt':
        return
    # Create a folder for cached files
    if not os.path.exists(cached_files_dir):
        os.makedirs(cached_files_dir)
    file_name = os.path.splitext(os.path.basename(file_path))[0]+'.txt' # extract only file name
    new_path = os.path.join(cached_files_dir,file_name)
    with open(file_path,'r') as inf:
        text = inf.read()
        with open(new_path,'w') as outf:
            outf.write(text)
            outf.close()
        inf.close()

# Compare line by line
# @input:  lines_1, lines_2 - lists(), where len(lines_1)>len(lines_2)
#          prefix = '--' when a cache file has more lines
#          prefix = '++' otherwise
# @output:
#    if in the lines are different return string "@l<number of line> +- <new line>"
#    further print remained lines from lines_1
def compare_lines(lines_1, lines_2, prefix):
    cnt = 0
    diff = ''
    for line in lines_2:
        if line!=lines_1[cnt]:
            diff+=' @l'+str(cnt+1)+' +- '+lines_1[cnt].rstrip()
        cnt+=1
    while cnt<len(lines_1):
        diff+=' @l'+str(cnt+1)+prefix+lines_1[cnt].rstrip()
        cnt+=1
    return diff


# Compare a file with the cached one
# @input: file_path
# @output: difference (str)
def compare_with_cached(file_path):
    difference = ''
    file_name = os.path.splitext(os.path.basename(file_path))[0]+'.txt'
    extention = os.path.splitext(os.path.basename(file_path))[1]
    if extention!='.txt':
        return ''
    cached_path = os.path.join(cached_files_dir,file_name)
    with open(file_path,'r') as file:
        with open(cached_path,'r') as cached_file:
            lines = file.readlines()
            lines_cached = cached_file.readlines()
            if len(lines_cached)<=len(lines):
                difference+=compare_lines(lines, lines_cached,' ++ ')
            else:
                difference+=compare_lines(lines_cached, lines,' -- ')
    return difference


# Read a file with a list of files to watch
# @input: str
# @output: list
def getFilesList(path):
    file_list=[]
    with open(path) as fp:
        for cnt, line in enumerate(fp):
            print("File {}: {}".format(cnt, line.rstrip()))
            file_list.append(line.rstrip())
        fp.close()
    print("-------\n")
    return file_list


def check_files(filenames):
    for nfile in filenames:
        if os.path.isfile(nfile):
            last_modification = os.stat(nfile).st_mtime # get a last modification date
            if nfile in _deleted_files: # when the file was deleted and appears again
                print('Added: {}'.format(nfile))
                _deleted_files.remove(nfile)
            if not nfile in _cached_last_time_files:
                _cached_last_time_files[nfile] = last_modification
                save_in_cache(nfile)
            if last_modification != _cached_last_time_files[nfile]:
                _cached_last_time_files[nfile] = last_modification
                diff = compare_with_cached(nfile)
                time_str =  time.strftime("%D %H:%M", time.localtime(last_modification))
                print('Modified {} | time {} | diff {} '.format(nfile,time_str,diff))
                save_in_cache(nfile)
        else:
            if nfile not in _deleted_files:
                _deleted_files.append(nfile)
                print('Deleted: {}'.format(nfile))


if __name__ == "__main__":
    source_file = sys.argv[1]
    print('Watching...'.format(source_file))
    filenames = getFilesList(source_file)
    while 1:
        try:
            time.sleep (1)
            check_files(filenames)
        except KeyboardInterrupt:
            print('\nDone')
            break
        except Exception as e:
            print(e)
