import ftplib

with ftplib.FTP('ftp-cdc.dwd.de') as ftp:
    try:

        ftp.login()
        files = []
        ftp.cwd('climate_environment/CDC/observations_germany/climate/hourly/air_temperature/historical/')
        ftp.dir(files.append)
        print(files)

        for file in files:
            filename = file.split()[8]
            with open(f'data_dwd/{filename}', 'wb') as f:
                ftp.retrbinary(f'RETR {filename}', f.write)

    except ftplib.all_errors as e:
        print(f'FTP error: {e}')

