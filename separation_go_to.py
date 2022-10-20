import os

def go_to_mainpath(mainpath):
    path = mainpath
    os.chdir(path)
    return path

def go_to_mix(mainpath):
    path = mainpath + '\mix'
    os.chdir(path)
    return path

def go_to_mix_folder(mainpath,foldname):
    path = go_to_mix(mainpath) + f'\{foldname}'
    os.chdir(path)
    return path

def go_to_mix_folder_activedir(mainpath, foldname, activedir):
    path = go_to_mix_folder(mainpath,foldname) + f'\{activedir}'
    os.chdir(path)
    return path

def go_to_separation(mainpath):
    path = mainpath + '\separation'
    os.chdir(path)
    return path

def go_to_separation_folder_activedir(mainpath, foldname, activedir):
    path = go_to_mix_folder(mainpath,foldname) + f'\{activedir}'
    os.chdir(path)
    return path

# def go_to_separation_foa(mainpath):
#     path = go_to_separation(mainpath) + '\\foa_dev'
#     os.chdir(path)
#     return path

# def go_to_separation_metadata(mainpath):
#     path = go_to_separation(mainpath) + '\metadata_dev'
#     os.chdir(path)
#     return path

