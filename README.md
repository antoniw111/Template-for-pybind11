# Intro
This repo contains my template for building CPP function as a module for python using pybind11 and scikit-build_core. I used pybind11 cmake_example as a base (https://github.com/pybind/cmake_example). I created this only for an educational purposes. Feel free to use and contribute. I am planning to ad a class template to his also. There is a PKGBUILD for Arch Linux also.
# Using on Arch Linux wth pacman and makepkg
To use this on arch simply download tar.gz file and in your folder use:
`makepkg`
This will build a zst file for pacman but won't install it.
Then you can go to .src/cmake_example folder which was created by *makepkg* and edit whatever you want.
After you are done simply:
`makepkg -ef`
This will not use tar.gz archive but **YOUR CHANGED CODE** in .src/cmake_example folder.
# Troubleshooting
- folder names like *cmake_example* are important but just for **PKGBUILD** file because there is hard coded module name which scikit will take and use with cmake.
