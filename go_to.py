import os

def go_to_project_dir(path_to_project_fold):
    os.chdir(path_to_project_fold)
def go_to_metadata_dir(path_to_project_fold):
    path = os.path.join(path_to_project_fold, 'metadata_dev')
    os.chdir(path)
def go_to_foa_dir(path_to_project_fold):
    path = os.path.join(path_to_project_fold, 'foa_dev')
    os.chdir(path)
def go_to_audio_entities_dev(path_to_project_fold):
    path = os.path.join(path_to_project_fold, 'wav_tunggal')
    os.chdir(path)
def go_to_mix_dev(path_to_project_fold):
    path = os.path.join(path_to_project_fold, 'mix_dev')
    os.chdir(path)
def go_to_history_dev(path_to_project_fold):
    path = os.path.join(path_to_project_fold, 'history_dev')
    os.chdir(path)
def go_to_wav_tunggal_cut(path_to_project_fold):
    path = os.path.join(path_to_project_fold, 'wav_tunggal_cut')
    os.chdir(path)
def go_to_mix_wav_tunggal_cut_overlap(path_to_project_fold):
    path = os.path.join(path_to_project_fold, 'mix_wav_tunggal_cut')
    os.chdir(path)