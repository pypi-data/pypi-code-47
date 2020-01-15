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
import yaml
import ntpath
import codecs
from zipfile import ZipFile
from colorama import init, Fore, Back, Style
from god_mode.metadata_rw import yaml_init

# -*- coding: utf-8 -*-

def main():

    init(autoreset=True)

    parser = argparse.ArgumentParser(description='Simple encryption/decryption script.')
    parser.add_argument('argFiles', nargs="*", type=str, help='List o files to encrypt/decrypt')
    parser.add_argument('-v','--verbose', help='Show what the script is doing.', action='store_true')
    parser.add_argument('-f','--files', help='File containing a list of files to encrypt/decrypt.', type=str)
    parser.add_argument('-d','--destination', help='Path to the encrypted/decrypted file(s). (Do NOT include any file or extension. Only the location to store the file(s).)', type=str, required=True)
    parser.add_argument('-m','--mode', help='Choose whether to encrypt or decrypt the file(s).', choices=['encrypt', 'decrypt'], type=str, required=True)
    parser.add_argument('-p','--password', help='The password to encrypt and decrypt the files.', type=str, required=True)
    parser.add_argument('-b','--buffer-multiplier', help='Choose the buffer size multiplier. (x * 1024). Default is 64. MUST BE THE SAME TO DECRYPT AND ENCRYPT.', default=64, type=int)
    parser.add_argument('-k','--kill', help="Choose this flag if you want to delete the original file when the encryption/decryption finish.", action='store_true')
    parser.add_argument('-e','--extension', help='Extension of the file(s) to be encrypted or decrypted.', default=".aes", type=str)
    parser.add_argument('--decryptor-file', help='File containing encrypted file information, such as original file name and original extension. To use this file, the name of the encrypted file must be the same as it was assigned.', type=str)
    args = parser.parse_args()

    decryptor = False
    # search for decrypt file
    if(args.mode == 'decrypt'):
        if args.decryptor_file:
            path, filename = os.path.split(args.decryptor_file)
            result = find(filename, path)
            if(result):
                metadataFile = True
                decryptor = True


    
    if args.verbose:
        print("[verbose]: Argument Passed Files ", args.argFiles)
        print('[verbose]: Files [',args.files,']')
        print('[verbose]: Destination [',args.destination,']')
        print('[verbose]: Mode [',args.mode,']')
        if(decryptor):
            print('[verbose]: Decryptor file given: ' + args.decryptor_file)
        print('[verbose]: Password [',args.password,']')
        print('[verbose]: Extension [',args.extension,']')
        print('[verbose]: Buffer Multiplier [',args.buffer_multiplier,']')
        #print('[verbose]: Real Buffer-Size [',bufferSize,']')
        print('[verbose]: Kill [',args.kill,']')
        print('[verbose]: Crypt version: 0.0.1b\n')

    noFiles = False
    noArgFiles = False

    if not args.files and not args.argFiles:
        if(args.mode == 'decrypt'):
            if(args.decryptor_file == '' or not metadataFile):
                print("Error: No files given.\n")               
                sys.exit()
        else:
            print("Error: No files given.\n")               
            sys.exit()

    if not args.files:
        noFiles = True
    if not args.argFiles:
        noArgFiles = True
    
    bufferSize = args.buffer_multiplier * 1024

    if not os.path.isfile(args.destination):
        if not os.path.exists(args.destination):
            print(Style.BRIGHT + Fore.WHITE + Back.RED + ' [Error]=> ' + Style.RESET_ALL + ' Destination "' + args.destination + '" not found. Use -h or --help.')
    else:
        print(Style.BRIGHT + Fore.WHITE + Back.RED + ' [Error]=> ' + Style.RESET_ALL + ' Destination cannot be a file. Use -h or --help.')

    if args.argFiles:
        for item in args.argFiles:
            if not os.path.exists(item):
                print(Style.BRIGHT + Fore.WHITE + Back.RED + ' [Error]=> ' + Style.RESET_ALL + ' Invalid argument: "' + item + '" Use -h or --help.')
                sys.exit(1)
            if not os.path.isfile(item):
                print(Style.BRIGHT + Fore.WHITE + Back.RED + ' [Error]=> ' + Style.RESET_ALL + ' Invalid argument: "' + item + '" Use -h or --help.')
                sys.exit(1)
    if args.files:
        if not os.path.exists(args.files):
            print(Style.BRIGHT + Fore.WHITE + Back.RED + ' [Error]=> ' + Style.RESET_ALL + ' File not found: "' + args.files + '" Use -h or --help.')
            sys.exit(1)



    if args.argFiles:
        for item in args.argFiles:
            if(args.mode == "encrypt"):
                generated_filename = str(uuid.uuid4())
                if(args.verbose):
                    print('Adding new encrypted file to metadata file.')
                try:
                    base = os.path.basename(item)
                    filename = os.path.splitext(base)[0]
                    extension = os.path.splitext(base)[1]
                    data = [[filename, generated_filename, extension, bufferSize]]
                    yaml_init(['w', args.destination + '/metadata.yaml', data, args.verbose])
                except:
                    print(Style.BRIGHT + Fore.WHITE + Back.RED + ' [Error]=> ' + Style.RESET_ALL + ' Unable to write metadata in: "' + args.destination + "/" + 'metadata.yaml' + '" Use -h or --help.')
                    sys.exit(1)

                print('Encrypting: ' + item)
                pyAesCrypt.encryptFile(item, args.destination + "/" + generated_filename + args.extension, args.password, bufferSize)
                
                if(args.kill):
                    os.remove(item)
                    print('File: "', item, '"Deleted (-k, --kill)"')
            
            elif(args.mode == "decrypt"):
                generated_filename = str(uuid.uuid4())
                
                print('Decrypting: ' + item)
                pyAesCrypt.decryptFile(item, args.destination + "/" + generated_filename + args.extension, args.password, bufferSize)
                
                if(args.kill):
                    os.remove(item)
                    print('File: "', item, '"Deleted (-k, --kill)"')

    names = []
    if args.files:
        lines = open(args.files, encoding='utf-8').read().split("\n")
        for item in lines:
            if not path_leaf(item) in names and item != '': 
                if(args.mode == "encrypt"):
                    generated_filename = str(uuid.uuid4())
                    if(args.verbose):
                        print('Adding new encrypted file to metadata file.')
                    try:
                        base = os.path.basename(item)
                        filename = os.path.splitext(base)[0]
                        extension = os.path.splitext(base)[1]
                        data = [[filename, generated_filename, extension, bufferSize]]
                        yaml_init(['w', args.destination + '/metadata.yaml', data, args.verbose])
                    except:
                        print(Style.BRIGHT + Fore.WHITE + Back.RED + ' [Error]=> ' + Style.RESET_ALL + ' Unable to write metadata in: "' + args.destination + "/" + 'metadata.yaml' + '" Use -h or --help.')
                        sys.exit(1)
                    print('Encrypting: ' + item)
                    pyAesCrypt.encryptFile(item, args.destination + "/" + generated_filename + args.extension, args.password, bufferSize)
                    if(args.kill):
                        os.remove(item)
                        print('File: "', item, '"Deleted (-k, --kill)"')
                elif(args.mode == "decrypt"):
                    generated_filename = str(uuid.uuid4())
                    print('Decrypting: ' + item)
                    pyAesCrypt.decryptFile(item, args.destination + "/" + generated_filename + args.extension, args.password, bufferSize)
                    if(args.kill):
                        os.remove(item)
                        print('File: "', item, '"Deleted (-k, --kill)"')

    if(decryptor):
        if(args.verbose):
            print('Decrypting via decryptor file.')
        # Get the path of the decryptor file
        # Where the files to decrypt are stored.
        path, filename = os.path.split(args.decryptor_file)

        # Decrypt the decryptor file
        pyAesCrypt.decryptFile(args.decryptor_file, path + "/metadata.yaml", args.password, (64 * 1024))

        # Loop through the files in $path
        # If one the file name match with one of the decryptor file,
        # Decrypts it with the data.
        fileData = yaml_init(['r', path + "/metadata.yaml", args.verbose])
        print('\nStarting...\n')
        counter = 0
        items = 0
        skip = 0
        for fileDecrypt in os.listdir(path):
            for item in fileData:
                if(item[1] == os.path.splitext(fileDecrypt)[0]):
                    if not find(item[0] + item[2], args.destination + '/'):
                        print(str(counter) + ': |' + fileDecrypt + '|')
                        pyAesCrypt.decryptFile(path + '/' + fileDecrypt, args.destination + '/' + item[0] + item[2], args.password, item[3])
                        if(args.kill):
                            os.remove(path + '/' + fileDecrypt)
                        counter += 1
                    else:
                        skip += 1
                        if(args.verbose):
                            print('Found duplicated. Skipping.')
            items += 1

        os.remove(path + "/metadata.yaml")
        if(args.kill):
            os.remove(args.decryptor_file)

        print('Decryption successful: ('+ str(counter) +' files decrypted out of '+ str(items) +') ('+ str(skip) +' skipped.)')

    if(args.mode == "encrypt"):
        print('Encrypting metadata file...')
        pyAesCrypt.encryptFile(args.destination + "/" + 'metadata.yaml', args.destination + "/libs.yaml", args.password, (64 * 1024))
        os.remove(args.destination + "/" + 'metadata.yaml')        

    print('done.')

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

if __name__ == "__main__":
    init(autoreset=True)
    main(sys.argv[1:])