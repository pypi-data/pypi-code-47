#!/usr/bin/python

'''

All thanks to https://pypi.org/project/pyAesCrypt/

Apache License

Version 2.0, January 2004

http://www.apache.org/licenses/

TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION

1. Definitions.

"License" shall mean the terms and conditions for use, reproduction, and distribution as defined by Sections 1 through 9 of this document.

"Licensor" shall mean the copyright owner or entity authorized by the copyright owner that is granting the License.

"Legal Entity" shall mean the union of the acting entity and all other entities that control, are controlled by, or are under common control with that entity. For the purposes of this definition, "control" means (i) the power, direct or indirect, to cause the direction or management of such entity, whether by contract or otherwise, or (ii) ownership of fifty percent (50%) or more of the outstanding shares, or (iii) beneficial ownership of such entity.

"You" (or "Your") shall mean an individual or Legal Entity exercising permissions granted by this License.

"Source" form shall mean the preferred form for making modifications, including but not limited to software source code, documentation source, and configuration files.

"Object" form shall mean any form resulting from mechanical transformation or translation of a Source form, including but not limited to compiled object code, generated documentation, and conversions to other media types.

"Work" shall mean the work of authorship, whether in Source or Object form, made available under the License, as indicated by a copyright notice that is included in or attached to the work (an example is provided in the Appendix below).

"Derivative Works" shall mean any work, whether in Source or Object form, that is based on (or derived from) the Work and for which the editorial revisions, annotations, elaborations, or other modifications represent, as a whole, an original work of authorship. For the purposes of this License, Derivative Works shall not include works that remain separable from, or merely link (or bind by name) to the interfaces of, the Work and Derivative Works thereof.

"Contribution" shall mean any work of authorship, including the original version of the Work and any modifications or additions to that Work or Derivative Works thereof, that is intentionally submitted to Licensor for inclusion in the Work by the copyright owner or by an individual or Legal Entity authorized to submit on behalf of the copyright owner. For the purposes of this definition, "submitted" means any form of electronic, verbal, or written communication sent to the Licensor or its representatives, including but not limited to communication on electronic mailing lists, source code control systems, and issue tracking systems that are managed by, or on behalf of, the Licensor for the purpose of discussing and improving the Work, but excluding communication that is conspicuously marked or otherwise designated in writing by the copyright owner as "Not a Contribution."

"Contributor" shall mean Licensor and any individual or Legal Entity on behalf of whom a Contribution has been received by Licensor and subsequently incorporated within the Work.

2. Grant of Copyright License. Subject to the terms and conditions of this License, each Contributor hereby grants to You a perpetual, worldwide, non-exclusive, no-charge, royalty-free, irrevocable copyright license to reproduce, prepare Derivative Works of, publicly display, publicly perform, sublicense, and distribute the Work and such Derivative Works in Source or Object form.

3. Grant of Patent License. Subject to the terms and conditions of this License, each Contributor hereby grants to You a perpetual, worldwide, non-exclusive, no-charge, royalty-free, irrevocable (except as stated in this section) patent license to make, have made, use, offer to sell, sell, import, and otherwise transfer the Work, where such license applies only to those patent claims licensable by such Contributor that are necessarily infringed by their Contribution(s) alone or by combination of their Contribution(s) with the Work to which such Contribution(s) was submitted. If You institute patent litigation against any entity (including a cross-claim or counterclaim in a lawsuit) alleging that the Work or a Contribution incorporated within the Work constitutes direct or contributory patent infringement, then any patent licenses granted to You under this License for that Work shall terminate as of the date such litigation is filed.

4. Redistribution. You may reproduce and distribute copies of the Work or Derivative Works thereof in any medium, with or without modifications, and in Source or Object form, provided that You meet the following conditions:

    You must give any other recipients of the Work or Derivative Works a copy of this License; and
    You must cause any modified files to carry prominent notices stating that You changed the files; and
    You must retain, in the Source form of any Derivative Works that You distribute, all copyright, patent, trademark, and attribution notices from the Source form of the Work, excluding those notices that do not pertain to any part of the Derivative Works; and
    If the Work includes a "NOTICE" text file as part of its distribution, then any Derivative Works that You distribute must include a readable copy of the attribution notices contained within such NOTICE file, excluding those notices that do not pertain to any part of the Derivative Works, in at least one of the following places: within a NOTICE text file distributed as part of the Derivative Works; within the Source form or documentation, if provided along with the Derivative Works; or, within a display generated by the Derivative Works, if and wherever such third-party notices normally appear. The contents of the NOTICE file are for informational purposes only and do not modify the License. You may add Your own attribution notices within Derivative Works that You distribute, alongside or as an addendum to the NOTICE text from the Work, provided that such additional attribution notices cannot be construed as modifying the License.

    You may add Your own copyright statement to Your modifications and may provide additional or different license terms and conditions for use, reproduction, or distribution of Your modifications, or for any such Derivative Works as a whole, provided Your use, reproduction, and distribution of the Work otherwise complies with the conditions stated in this License.

5. Submission of Contributions. Unless You explicitly state otherwise, any Contribution intentionally submitted for inclusion in the Work by You to the Licensor shall be under the terms and conditions of this License, without any additional terms or conditions. Notwithstanding the above, nothing herein shall supersede or modify the terms of any separate license agreement you may have executed with Licensor regarding such Contributions.

6. Trademarks. This License does not grant permission to use the trade names, trademarks, service marks, or product names of the Licensor, except as required for reasonable and customary use in describing the origin of the Work and reproducing the content of the NOTICE file.

7. Disclaimer of Warranty. Unless required by applicable law or agreed to in writing, Licensor provides the Work (and each Contributor provides its Contributions) on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied, including, without limitation, any warranties or conditions of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A PARTICULAR PURPOSE. You are solely responsible for determining the appropriateness of using or redistributing the Work and assume any risks associated with Your exercise of permissions under this License.

8. Limitation of Liability. In no event and under no legal theory, whether in tort (including negligence), contract, or otherwise, unless required by applicable law (such as deliberate and grossly negligent acts) or agreed to in writing, shall any Contributor be liable to You for damages, including any direct, indirect, special, incidental, or consequential damages of any character arising as a result of this License or out of the use or inability to use the Work (including but not limited to damages for loss of goodwill, work stoppage, computer failure or malfunction, or any and all other commercial damages or losses), even if such Contributor has been advised of the possibility of such damages.

9. Accepting Warranty or Additional Liability. While redistributing the Work or Derivative Works thereof, You may choose to offer, and charge a fee for, acceptance of support, warranty, indemnity, or other liability obligations and/or rights consistent with this License. However, in accepting such obligations, You may act only on Your own behalf and on Your sole responsibility, not on behalf of any other Contributor, and only if You agree to indemnify, defend, and hold each Contributor harmless for any liability incurred by, or claims asserted against, such Contributor by reason of your accepting any such warranty or additional liability.

END OF TERMS AND CONDITIONS
'''

import sys
import pyAesCrypt
import getopt
import os
import io
import errno
import tempfile
import uuid
import re
import argparse
import json 
import ntpath
import codecs
from binaryornot.check import is_binary
from pathlib import Path
from zipfile import ZipFile
from colorama import init, Fore, Back, Style

# -*- coding: utf-8 -*-

def main(argv):
    parser = argparse.ArgumentParser(description='Simple encryption/decryption script.')
    parser.add_argument('argFiles', nargs="*", type=str, help='List o files to encrypt/decrypt')
    parser.add_argument('-v','--verbose', help='Show what the script is doing.', action='store_true')
    parser.add_argument('-F','--files', help='File containing a list of files to encrypt/decrypt.', type=str)
    parser.add_argument('-d','--destination', help='Path to the encrypted/decrypted file(s). (Do NOT include any file or extension. Only the location to store the file(s).)', type=str, required=True)
    parser.add_argument('-m','--mode', help='Choose whether to encrypt or decrypt the file(s).', choices=['encrypt', 'decrypt'], type=str, required=True)
    parser.add_argument('-p','--password', help='The password to encrypt and decrypt the files.', type=str, required=True)
    parser.add_argument('-b','--buffer-multiplier', help='Choose the buffer size multiplier. (x * 1024). Default is 64. MUST BE THE SAME TO DECRYPT AND ENCRYPT.', default=64, type=int)
    parser.add_argument('-k','--kill', help="Choose this flag if you want to delete the original file when the encryption/decryption finish.", action='store_true')
    parser.add_argument('-e','--extension', help='Extension of the file(s) to be encrypted or decrypted.', default=".aes", type=str, required=True)
    parser.add_argument('--decryptor-file', help='File containing encrypted file information, such as original file name and original extension. To use this file, the name of the encrypted file must be the same as it was assigned.', default=None, type=str)
    args = parser.parse_args()

    bufferSize = args.buffer_multiplier * 1024

    cwd = os.getcwd()

    if args.destination == "." or args.destination == "./":
        args.destination = cwd

    dec_file = ''

    if args.extension[0] != '.':
        args.extension = '.' + args.extension

    is_dec_file_non_existent = False
    
    if not args.decryptor_file:
        found = False
        for file in os.listdir(args.destination):
            if file == 'libs.json':
                print('found decryptor file: ' + os.path.join(args.destination, file))
                dec_file = os.path.join(args.destination, file)
                found = True
                break
        if not found:
            path = os.path.join(args.destination, 'libs.json')
            open(path, 'a', encoding="utf8").close()
            is_dec_file_non_existent = True
            dec_file = path
    else:
        if not os.path.isfile(args.decryptor_file):
            print('The decryptor file does not exist... creating')
            open(args.decryptor_file, 'a', encoding="utf8").close()
            is_dec_file_non_existent = True
            dec_file = args.decryptor_file

    is_dec_encrypted = False

    ## Check if decryptor file is encrypted
    ## library isbinaryornot : https://binaryornot.readthedocs.io/
    is_dec_encrypted = is_binary('./libs.json')


    dec_file_abs_dir = os.path.dirname(os.path.abspath(dec_file))

    if args.verbose:
        print("[verbose]: Argument Passed Files ", args.argFiles)
        print('[verbose]: Files [',args.files,']')
        print('[verbose]: Destination [',args.destination,']')
        print('[verbose]: Mode [',args.mode,']')
        print('[verbose]: Decryptor file [',dec_file,']')
        print('[verbose]: Password [',args.password,']')
        print('[verbose]: Extension [',args.extension,']')
        print('[verbose]: Buffer Multiplier [',args.buffer_multiplier,']')
        print('[verbose]: Real Buffer-Size [',bufferSize,']')
        print('[verbose]: Kill [',args.kill,']')
        print('[verbose]: Crypt version: 1.0.0a\n')

    if args.argFiles:
        if args.mode == 'encrypt':
            encrypt_files(args.argFiles, args.destination, args.extension, args.password, bufferSize, args.verbose, dec_file, is_dec_encrypted, dec_file_abs_dir)
        elif args.mode == 'decrypt':
            decrypt_files(args.argFiles, args.destination, args.extension, args.password, bufferSize, args.verbose, dec_file, is_dec_encrypted, dec_file_abs_dir, is_dec_file_non_existent)

    elif args.files:
        lines = open(args.files, encoding='utf-8').read().split("\n")
        if args.mode == 'encrypt':
            encrypt_files(lines, args.destination, args.extension, args.password, bufferSize, args.verbose, dec_file, is_dec_encrypted, dec_file_abs_dir)
        elif args.mode == 'decrypt':
            decrypt_files(lines, args.destination, args.extension, args.password, bufferSize, args.verbose, dec_file, is_dec_encrypted, dec_file_abs_dir, is_dec_file_non_existent)
    else:
        print_error("No files supplied.")

def path_leaf(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)

def getSize(path):
    st = os.stat(path)
    return st.st_size

def find(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)

def print_error(msg):
    print(Style.BRIGHT + Fore.WHITE + Back.RED + ' [Error]=> ' + Style.RESET_ALL + msg)

def encrypt_files(files, destination, extension, password, bufferSize, verbose, dec_file, is_dec_encrypted, dec_file_abs_dir):
    for item in files:
        if not os.path.isfile(item):
            print_error('A given file could not be found or its not a readable file. Skipping.')
            continue

        generated_filename = str(uuid.uuid4()) # Create a random name for the file
        data = {'file': {'generated': generated_filename, 'buffer-ratio': bufferSize, 'size': getSize(item), 'name': path_leaf(item), 'ext': extension}}
        temp_dec = os.path.join(dec_file_abs_dir, 'libs.json.temp')
        try:
            if(verbose):
                print("Encrypting " + item)
            pyAesCrypt.encryptFile(item, destination + "/" + generated_filename + extension, password, bufferSize)
            try:
                if is_dec_encrypted:
                    if(verbose):
                        print("Trying to decrypt decryptor file...")

                    pyAesCrypt.decryptFile(dec_file, temp_dec, password, (64 * 1024))
                    data_temp = []
                    try:
                        with open(temp_dec, encoding="utf8") as json_file:
                            data_temp = json.load(json_file)
                        data_temp.append(data)
                    except Exception as ex:
                        print(str(ex) + "\n shine")

                    os.remove(dec_file)

                    with open(dec_file, 'w', encoding="utf8") as outfile:
                        json.dump(data_temp, outfile, sort_keys=True, indent=4)
                else:
                    data_temp = []
                    if os.stat(dec_file).st_size > 0:
                        with open(dec_file, encoding="utf8") as json_file:
                            data_temp = json.load(json_file)
                    
                    data_temp.append(data)
                    
                    os.remove(dec_file)

                    with open(temp_dec, 'w', encoding="utf8") as outfile:
                        json.dump(data_temp, outfile, sort_keys=True, indent=4)

                    #encrypt decyptor file
                    pyAesCrypt.encryptFile(temp_dec, dec_file, password, (64 * 1024))

                    os.remove(temp_dec)
            except Exception as e:
                print_error(str(e) + "\nCould not decrypt the decryptor file...")
        except Exception as e:
            print_error(str(e) + "\nCould not encrypt file. Skipping.")
    print('done')

def decrypt_files(files, destination, extension, password, bufferSize, verbose, dec_file, is_dec_encrypted, dec_file_abs_dir, is_dec_file_non_existent):
    data_temp = []
    temp_dec = os.path.join(dec_file_abs_dir, 'libs.json.temp')
    
    if is_dec_encrypted:
        if verbose:
           print('Decrypting decryptor file...')
                
        pyAesCrypt.decryptFile(dec_file, temp_dec, password, (64 * 1024))
        try:
            with open(temp_dec, encoding="utf8") as json_file:
                data_temp = json.load(json_file)
        except Exception as ex:
            print(str(ex) + "\n shine")
    counter = 0
    for item in files:
        if not os.path.isfile(item):
            print_error('A given file could not be found or its not a readable file. Skipping.')
            continue
    
    if not is_dec_file_non_existent:
        if is_dec_encrypted:
            if verbose:
                print('Decrypting file...')

            try:
                actual_data_file = {}
            
                for dat in data_temp:
                    if dat['file']['generated'] in item:
                        actual_data_file = dat['file']
                        break
                if verbose:
                    print('Found metadata in the decryptor file')
                    print('Decrypting...')
    
                final_file_dest = os.path.join(destination, actual_data_file['name']) 

                pyAesCrypt.decryptFile(item, final_file_dest, password, actual_data_file['buffer-ratio'])
                print('good')
            except Exception as ex:
                print_error(str(ex))
                try:
                    print('Decrypting...')
                    pyAesCrypt.decryptFile(item, "guessed_" + item +".no.ext", password, bufferSize)
                    print('good')
                except:
                    print_error('Guessed decryption failed... skipping')
    else:
        print('not yet implemented')
        ## TODO ##
        # -F not working properly
        # -k not working
    
    os.remove(temp_dec)

    print('done')
if __name__ == "__main__":
    init(autoreset=True)
    main(sys.argv[1:])
