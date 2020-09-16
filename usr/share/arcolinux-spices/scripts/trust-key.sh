#!/bin/bash
echo "Receiving, local signing and refreshing keys"
#erik
pacman-key -r 74F5DE85A506BF64
pacman-key --lsign-key 74F5DE85A506BF64
#marco
pacman-key -r F1ABB772CE9F7FC0
pacman-key --lsign-key F1ABB772CE9F7FC0
#john
pacman-key -r 4B1B49F7186D8731
pacman-key --lsign-key 4B1B49F7186D8731
#stephen
pacman-key -r 02D507C6EFB8CEAA
pacman-key --lsign-key 02D507C6EFB8CEAA

sudo pacman-key --refresh-keys
echo "###                 ArcoLinux key trusted                      ####"
