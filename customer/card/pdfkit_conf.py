import os, subprocess, platform
import pdfkit

if platform.system() == 'Windows':
    pdfkit_config = pdfkit.configuration(wkhtmltopdf=os.environ.get('WKHTMLTOPDF_PATH','C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe'))
if 'DYNO' in os.environ:
    print ('loading wkhtmltopdf path on heroku')
    WKHTMLTOPDF_CMD = subprocess.Popen(['which', os.environ.get('WKHTMLTOPDF_BINARY', 'wkhtmltopdf-pack')], stdout=subprocess.PIPE).communicate()[0].strip()
else:
    WKHTMLTOPDF_CMD = subprocess.Popen(['which', os.environ.get('WKHTMLTOPDF_PATH', 'wkhtmltopdf')],stdout=subprocess.PIPE).communicate()[0].strip()
    pdfkit_config = pdfkit.configuration(wkhtmltopdf=WKHTMLTOPDF_CMD)

