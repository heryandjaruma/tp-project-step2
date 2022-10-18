import nussl
import numpy as np
import sox
import pandas as pd
from colorama import Fore

from separation_go_to import *
from Classes.AudioEntity import AudioEntity
from Classes.OvEntity import OvEntity

# TODO: will get all files in the given range implicitly
def get_all_files_in_metadata_dev(first_fold_number:int, last_fold_number:int, path_to_project_fold, mix_foldname):
    # go_to_mix_folder_activedir(path_to_project_fold,mix_foldname,'metadata_dev')
    all_list = [file for file in os.listdir() if 'ov2' not in file]
    returned_list_list = []
    for item in range(first_fold_number, last_fold_number+1):
        returned_list = [file for file in all_list if ('fold' + str(item)) in file]
        if returned_list:
            returned_list_list.append(returned_list)
        else:
            print(Fore.RED, 'fold', item, 'does not exist... try checking your file', Fore.WHITE)
            last_fold_number = last_fold_number-1
    # go_to_mix_folder(path_to_project_fold,mix_foldname)                             # go to project
    return returned_list_list, last_fold_number     #! RETURN list of list and last folder number that is valid

# TODO: to initialize all objects from files
def init_all_objects(list_of_files, path_to_project_fold, ):
    main_object_list = []
    for foldlist in list_of_files:
        object_list = []
        for item in foldlist:
            object_list.append(OvEntity(item, path_to_project_fold))
            object_list[-1].create_me(path_to_project_fold)
        main_object_list.append(object_list)
    return main_object_list

if __name__ == '__main__':
    os.system('cls')

    mainpath = r'D:\TPProject\STEP2_separation' # main path

    go_to_mix(mainpath)     # go to mix folder inside mainpath

    folders=os.listdir()
    for f in folders:   # foreach mix item\

        project_path_only = go_to_mix_folder(mainpath,f)

        go_to_mix_folder_activedir(mainpath,f,'history_dev') # go to history dir
        histories = os.listdir()
        for h in histories: # foreach history_dev item            

            # TODO: read csv to get history df
            history_df = pd.read_csv(h, header=None)
            for index, r in history_df.iterrows(): # foreach row in iterrows

                # TODO: init 2 related OvEntity again
                oe1filename = r[0][:-4] + '.csv'
                oe2filename = r[1][:-4] + '.csv'

                ovs = []

                ovs.append(OvEntity(oe1filename, project_path_only))
                ovs.append(OvEntity(oe2filename, project_path_only))

                # trus coba ke 5 fold pake 'if not 1,2,3, etc : continue'

                # MAPPING
                # 0 -> 0e1
                # 1 -> 0e2
                # 2 -> class ae1
                # 3 -> class ae2
                # 4 -> mix
                # 5 -> ae1 tunggal cut
                # 6 -> ae2 tunggal cut
                # 7 -> mix tunggal cut

                # TODO: get dataMix
                dataMix_name = r[7]
                dataMix_fullpath = go_to_mix_folder_activedir(mainpath,f,'mix_wav_tunggal_cut') + f'\{dataMix_name}'
                dataMix = nussl.AudioSignal(dataMix_fullpath)
                # print(type(dataMix))

                for loop_ke, i in enumerate(range(5,7)):  # loop 2 times for each overlapping audio

                    # TODO: get singleMix
                    dataSingle_name = r[i]
                    dataSingle_fullpath = go_to_mix_folder_activedir(mainpath,f,'wav_tunggal_cut') + f'\{dataSingle_name}'
                    dataSingle = nussl.AudioSignal(dataSingle_fullpath)
                    # print(type(dataSingle))

                    # TODO: then export
                    mask_data = (
                        np.abs(dataSingle.stft()) /
                        np.maximum(
                        np.abs(dataMix.stft()),
                        np.abs(dataSingle.stft())
                        ) + nussl.constants.EPSILON
                    )

                    magnitude, phase = np.abs(dataMix.stft_data), np.angle(dataMix.stft_data)
                    masked_abs = magnitude * mask_data
                    masked_stft = masked_abs * np.exp(1j * phase)

                    drum_est = dataMix.make_copy_with_stft_data(masked_stft)
                    drum_est.istft()

                    naming = go_to_mix_folder_activedir(mainpath,f,'separation_wav_tunggal_cut')
                    export_fullpath = naming + '\\' + r[5]
                    export_fullpath = export_fullpath[:-4] + f'_{loop_ke+1}_HasilSeparated.wav'
                    drum_est.write_audio_to_file(export_fullpath,sample_rate=24000)

                    # TODO: append type of class 
                    audioclass = []
                    audioclass.append(r[2])
                    audioclass.append(r[3])

                    # get current metadata
                    main_df = ovs[0].get_df()
                    
                    
                    


                    input()