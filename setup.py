from distutils.core import setup


setup(
  name = 'Lykan',        
  packages = ['Lykan'],   
  version = '0.1',      
  license='MIT',        
  description = 'This procject is use to extract all type of from some specific file like Doxc, ppt, txt, csv, jpg, png and etc. ',   # Give a short description about your library
  author = 'KUNAL MALHOTRA',                  
  author_email = 'kunal9988243618@gmail.com',      
  url = 'https://github.com/Gareeeb7/Lykan',  
  download_url = 'https://github.com/user/reponame/archive/v_01.tar.gz',  
  keywords = ['pdf_To_Text("file_name")', 'docx_To_Text("file_name")', 'load_Text("file_name")', 'ppt_To_Text("file_name")', 'image_To_Text("file_name")','csv_Load("file_name")'],   # Keywords that define your package best
  install_requires=[          
          'pandas',
          'glob',
          'cv2',
          'pytesseract',
          'pptx',
          'docx',
          'PyPDF2',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',     
    'Intended Audience :: Developers',      
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',  
    'Programming Language :: Python :: 3',     
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
  ],
)
