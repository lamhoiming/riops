"""This is a script to save riops .nc files from thredds server and read ice thickness.2019-02-14 Lam Hoi Ming"""#%% Import librariesimport urllibimport globimport osimport h5pyimport netCDF4 as nc4from tqdm import tqdm#%% Define functions and classesclass DownloadProgressBar(tqdm):    def update_to(self, b=1, bsize=1, tsize=None):        if tsize is not None:            self.total = tsize        self.update(b * bsize - self.n)def download_url(fileurl, output_path):    with DownloadProgressBar(unit='B', unit_scale=True,                             miniters=1, desc=fileurl.split('/')[-1]) as t:        urllib.request.urlretrieve(fileurl, filename=output_path, reporthook=t.update_to)#%%##        #%% Define start and end datesstartdate = input('What is the starting date (yyyymmdd)?')enddate = input('What is the end date (yyyymmdd)?') or ''date = startdate#%% Julian day counter # Taken from Enno Middleberg's site of useful astronomical python references: http://www.astro.rub.de/middelberg/python/python.html# Adopted by Lam Hoi Ming 2019-02-14def julianday(date):        yyyy = int(date[0:4])    mm = int(date[4:6])    dd = int(date[6:8])            # Now calculate the fractional year. Do we have a leap year?     daylist=[31,28,31,30,31,30,31,31,30,31,30,31]    daylist2=[31,29,31,30,31,30,31,31,30,31,30,31]    if (yyyy%4 != 0):        days=daylist    elif (yyyy%400 == 0):        days=daylist2    elif (yyyy%100 == 0):        days=daylist    else:        days=daylist2        # Counting from zero (python convention)    daysum = 0    for y in range(mm - 1):        daysum = daysum + days[y]    ju_day = daysum + dd - 1    print(ju_day)#%% Julian day to yyyyddmm format# Task to convert a list of julian dates to gregorian dates# description at http://mathforum.org/library/drmath/view/51907.html# Original algorithm in Jean Meeus, "Astronomical Formulae for Calculators# Adopted by Lam Hoi Ming 2019-02-14#%% Retrieve files from url path and save on local disksavedir = input('Where to save?') or "D:/Data/RIOPS/" #%% Retrieve files from url path and save on local disksavedir = input('Where to save?') or "D:/Data/RIOPS/" fileurl = 'http://navigator.oceansdata.ca/thredds/fileServer/riops/daily/' + startdate + '_2D.nc'  #2D files contain ice and snow datatmp_filename = startdate + '_2D.nc'output_path = savedir + tmp_filenamefexist = os.path.isfile(output_path) # check if the file already existsif fexist:    print('This file already exists!')else:    download_url(fileurl, output_path)print('Select another file or date range')#%% Test reading ice thickness data from one filenc = nc4.Dataset(output_path,'r')print(nc.variables.keys()) # Display variable metadata with netCDF4for key in nc.variables.keys():    print(nc.variables[key])nc.close()    f = h5py.File(output_path,'r')icevol = f['iicevol'][:]snowvol = f['isnowvol'][:]#%% Loop over downloaded dataset to get ice and snow thicknessfor file in glob.glob():    