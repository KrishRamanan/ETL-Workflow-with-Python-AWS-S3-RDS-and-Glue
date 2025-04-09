## Downloading and unziping the zipfile using CMD

1. Extract data from Web to Local Machine:
	
	Step1: By Using command line we can extract the data from source by using

			wget [Link]

			Note: wget is a command line code which used to download a file from web source

			Make sure wget is added in your Windows/System32

	Step2: Since the souce file is in ZIP format, we need to unzip the file so

			tar -xf[file.zip] -C [Directory in which you need to extract]

			Note: tar is used to combine to a single file and viversa

			-f <filename>  Location of archive
			-C <dir>  Change to <dir> before processing remaining files

	Command Line Code:

				C:\Learn\Project>wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0221EN-SkillsNetwork/labs/module%206/Lab%20-%20Extract%20Transform%20Load/data/source.zip
				--2025-04-05 20:43:00--  https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0221EN-SkillsNetwork/labs/module%206/Lab%20-%20Extract%20Transform%20Load/data/source.zip
				Resolving cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud (cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud)... 169.63.118.104
				Connecting to cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud (cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud)|169.63.118.104|:443... connected.
				HTTP request sent, awaiting response... 200 OK
				Length: 2707 (2.6K) [application/zip]
				Saving to: 'source.zip'

				source.zip                    100%[=================================================>]   2.64K  --.-KB/s    in 0s

				2025-04-05 20:43:02 (100 MB/s) - 'source.zip' saved [2707/2707]


				C:\Learn\Project>mkdir UnzipRawFile

				C:\Learn\Project>tar -xf source.zip -C C:\Learn\Project\UnzipRawFile

## Uploading Local Files to AWS S3 by using Boto3

    Step1: Make sure that you install boto3 to your python Environment

            pip install boto3

    Step2: Capture the relevent data from S3
        Details like:
            AWS_A - Based on IAM
			AWS_S - Based on IAM
			AWS_BUCKET_NAME - Bucket Name which you have created in S3
			AWS_REGION - as name indigates it describes abou region
			LOCAL_FOLDER - local file directory
			S3_PREFIX - Name what you need to be renamed in S3

	Step3: Config File
		Based on the input config the AmazonS3Upload.py file and run it