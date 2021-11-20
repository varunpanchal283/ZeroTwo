from __future__ import print_function
from threading import *
from PyQt5.QtCore import *
from PyQt5 import QtCore
from PyQt5 import QtGui
from google_auth_oauthlib.flow import Flow, InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload, MediaIoBaseDownload
from google.auth.transport.requests import Request
from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtWidgets
from parse_url import parse_url
from six.moves import urllib_parse
#from Google import Create_Service
from PyQt5.QtWidgets import QDialog,QMainWindow, QApplication, QFileDialog
from PyQt5.uic import loadUi

import pickle
import sys
import glob
import json
import os
import os.path as osp
import re
import shutil
import sys
import tempfile
import textwrap
import time
import warnings
import requests
import six
import tqdm


global progess_total
global curr_progress
progess_total=0
curr_progress=0

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(887, 543)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 20, 221, 501))
        self.widget.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.506, y1:0, x2:0.517, y2:1, stop:0 rgba(143, 173, 171, 255), stop:0.585227 rgba(84, 114, 178, 255), stop:1 rgba(24, 53, 184, 255));\n"
"border-radius: 20px;")
        self.widget.setObjectName("widget")
        self.connect = QtWidgets.QPushButton(self.widget)
        self.connect.setGeometry(QtCore.QRect(70, 150, 81, 81))
        self.connect.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 75 9pt \"Agency FB\";\n"
"font-weight: Bold;\n"
"border-radius: 40px;\n"
"")
        self.connect.setObjectName("connect")
        self.exit = QtWidgets.QPushButton(self.widget)
        self.exit.setGeometry(QtCore.QRect(70, 440, 75, 23))
        self.exit.setStyleSheet("background-color: rgb(167, 58, 7);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.exit.setObjectName("exit")
        self.rezero = QtWidgets.QWidget(self.centralwidget)
        self.rezero.setGeometry(QtCore.QRect(200, 20, 671, 501))
        self.rezero.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0.489, x2:1, y2:0.517, stop:0 rgba(255, 255, 255, 255), stop:0.977273 rgba(204, 250, 221, 255));\n"
"border-radius: 20px;")
        self.rezero.setObjectName("rezero")
        self.inputid = QtWidgets.QLineEdit(self.rezero)
        self.inputid.setGeometry(QtCore.QRect(160, 40, 481, 31))
        self.inputid.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 8pt \"Papyrus\";")
        self.inputid.setObjectName("inputid")
        self.logo = QtWidgets.QTextEdit(self.rezero)
        self.logo.setGeometry(QtCore.QRect(70, 360, 571, 91))
        self.logo.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(255, 114, 246, 255), stop:0.375 rgba(153, 132, 225, 255), stop:0.613636 rgba(96, 138, 248, 255), stop:1 rgba(245, 147, 201, 255));\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Centaur\";\n"
"font-weight: bold;\n"
"border-radius: 0px;")
        self.logo.setObjectName("logo")
        self.getinfo = QtWidgets.QPushButton(self.rezero)
        self.getinfo.setGeometry(QtCore.QRect(70, 40, 75, 31))
        self.getinfo.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0.489, x2:1, y2:0.489, stop:0 rgba(147, 122, 255, 255), stop:0.982955 rgba(255, 171, 171, 255));\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"font: 75 10pt \"Agency FB\";\n"
"font-weight: Bold;\n"
"")
        self.getinfo.setObjectName("getinfo")
        self.dirchooser = QtWidgets.QPushButton(self.rezero)
        self.dirchooser.setGeometry(QtCore.QRect(70, 320, 121, 31))
        self.dirchooser.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0.489, x2:1, y2:0.489, stop:0 rgba(147, 122, 255, 255), stop:0.982955 rgba(255, 171, 171, 255));\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"font: 75 10pt \"Agency FB\";\n"
"font-weight: Bold;\n"
"")
        self.dirchooser.setObjectName("dirchooser")
        self.download = QtWidgets.QPushButton(self.rezero)
        self.download.setGeometry(QtCore.QRect(550, 320, 91, 31))
        self.download.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0.489, x2:1, y2:0.489, stop:0 rgba(147, 122, 255, 255), stop:0.982955 rgba(255, 171, 171, 255));\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"font: 75 10pt \"Agency FB\";\n"
"font-weight: Bold;\n"
"")
        self.download.setObjectName("download")
        self.listid = QtWidgets.QTableWidget(self.rezero)
        self.listid.setEnabled(True)
        self.listid.setGeometry(QtCore.QRect(70, 90, 571, 211))
        self.listid.setStyleSheet("font: 10pt \"Centaur\";\n"
"font-weight: bold;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(114, 190, 255, 255), stop:0.375 rgba(153, 132, 225, 255), stop:0.613636 rgba(96, 138, 248, 255), stop:1 rgba(148, 192, 194, 255));\n"
"color: rgb(255, 255, 255);\n"
"font-weight: bold;\n"
"border-radius: 0px;")
        self.listid.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.listid.setFrameShadow(QtWidgets.QFrame.Plain)
        self.listid.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.listid.setProperty("showDropIndicator", False)
        self.listid.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.listid.setShowGrid(False)
        self.listid.setGridStyle(QtCore.Qt.NoPen)
        self.listid.setWordWrap(False)
        self.listid.setObjectName("listid")
        self.listid.setColumnCount(5)
        self.listid.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.listid.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.listid.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.listid.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.listid.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.listid.setHorizontalHeaderItem(4, item)
        self.listid.horizontalHeader().setVisible(False)
        self.listid.horizontalHeader().setHighlightSections(False)
        self.listid.verticalHeader().setVisible(False)
        self.listid.verticalHeader().setHighlightSections(False)
        self.progress = QtWidgets.QProgressBar(self.rezero)
        self.progress.setGeometry(QtCore.QRect(70, 460, 571, 23))
        self.progress.setAutoFillBackground(False)
        self.progress.setProperty("value", 0)
        self.progress.setTextVisible(False)
        self.progress.setObjectName("progress")
        self.dirlabel = QtWidgets.QLineEdit(self.rezero)
        self.dirlabel.setEnabled(True)
        self.dirlabel.setGeometry(QtCore.QRect(200, 320, 331, 31))
        self.dirlabel.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 8pt \"Papyrus\";\n"
"")
        self.dirlabel.setObjectName("dirlabel")
        self.rezero.raise_()
        self.widget.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.connect.setText(_translate("MainWindow", "CONNECT"))
        self.exit.setText(_translate("MainWindow", "EXIT"))
        self.getinfo.setText(_translate("MainWindow", "Get Info"))
        self.dirchooser.setText(_translate("MainWindow", "Choose Directory"))
        self.download.setText(_translate("MainWindow", "Download"))
        self.listid.setSortingEnabled(False)
        item = self.listid.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "blank space"))
        item = self.listid.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "File Name"))
        item = self.listid.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Type"))
        item = self.listid.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Size"))
        item = self.listid.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Progress"))


class WorkerThread(QThread):
	update_progress=pyqtSignal(list)
	terminal_progress=pyqtSignal(str)
	msg_progress=pyqtSignal(bool)
	def run(self):
		use_cookies=True
		verify=True
		proxy=None
		speed=None
		quiet=False
		resume=False
		global set_id
		global fname
		dc=0
		zerotwo=False
		for i in set_id:
			dc+=1
			url="https://drive.google.com/uc?id="+i
			if fname[-1]!="/":
				fname=fname+"/"
			fff=fname+set_id[i][0]
			fff=fff.replace("/","\\")
			if not os.path.exists(fff):
				os.makedirs(fff)
			output=fff+set_id[i][1]
			CHUNK_SIZE = 512 * 1024
			home = osp.expanduser("~")
			url_origin = url
			sess = requests.session()
			cache_dir = osp.join(home, ".cache", "gdown")
			if not osp.exists(cache_dir):
				os.makedirs(cache_dir)
			cookies_file = osp.join(cache_dir, "cookies.json")
			if osp.exists(cookies_file) and use_cookies:
				with open(cookies_file) as f:
					cookies = json.load(f)
				for k, v in cookies:
					sess.cookies[k] = v
			if proxy is not None:
				sess.proxies = {"http": proxy, "https": proxy}
				print("Using proxy:", proxy, file=sys.stderr)
			parsed = urllib_parse.urlparse(url)
			query = urllib_parse.parse_qs(parsed.query)
			is_gdrive = parsed.hostname in ["drive.google.com", "docs.google.com"]
			is_download_link = parsed.path.endswith("/uc")
			file_id = None
			if "id" in query:
				file_ids = query["id"]
				if len(file_ids) == 1:
					file_id = file_ids[0]
			else:
				patterns = [r"^/file/d/(.*?)/view$", r"^/presentation/d/(.*?)/edit$"]
				for pattern in patterns:
					match = re.match(pattern, parsed.path)
					if match:
						file_id = match.groups()[0]
						break
			gdrive_file_id, is_gdrive_download_link = file_id, is_download_link
			url = "https://drive.google.com/uc?id={id}".format(id=gdrive_file_id)
			url_origin = url
			is_gdrive_download_link = True
			headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36"}
			while True:
				try:
					res = sess.get(url, headers=headers, stream=True, verify=verify)
				except requests.exceptions.ProxyError as e:
					print("An error has occurred using proxy:", proxy, file=sys.stderr)
					print(e, file=sys.stderr)
					return
				with open(cookies_file, "w") as f:
					cookies = [
		                (k, v)
		                for k, v in sess.cookies.items()
		                if not k.startswith("download_warning_")
		            ]
					json.dump(cookies, f, indent=2)
				if "Content-Disposition" in res.headers:
					break
				if not (gdrive_file_id and is_gdrive_download_link):
					break
				try:
					url = ""
					contents=res.text
					for line in contents.splitlines():
						m = re.search(r'href="(\/uc\?export=download[^"]+)', line)
						if m:
							url = "https://docs.google.com" + m.groups()[0]
							url = url.replace("&amp;", "&")
							break
						m = re.search("confirm=([^;&]+)", line)
						if m:
							confirm = m.groups()[0]
							url = re.sub(r"confirm=([^;&]+)", r"confirm={}".format(confirm), url)
							break
						m = re.search('"downloadUrl":"([^"]+)', line)
						if m:
							url = m.groups()[0]
							url = url.replace("\\u003d", "=")
							url = url.replace("\\u0026", "&")
							break
						m = re.search('<p class="uc-error-subcaption">(.*)</p>', line)
				except:
					print("Access denied with the following error:")
					#print(contents)
					return
			p_count=0
			if gdrive_file_id and is_gdrive_download_link:
				m = re.search('filename="(.*)"', res.headers["Content-Disposition"])
				filename_from_url = m.groups()[0]
			else:
				filename_from_url = osp.basename(url)
			if output is None:
				output = filename_from_url
			output_is_path = isinstance(output, six.string_types)
			if output_is_path and output.endswith(osp.sep):
				if not osp.exists(output):
					os.makedirs(output)
				output = osp.join(output, filename_from_url)
			if output_is_path:
				existing_tmp_files = glob.glob("{}*".format(output))
				if resume and existing_tmp_files:
					tmp_file = existing_tmp_files[0]
				else:
					resume = False
					tmp_file = tempfile.mktemp(suffix=tempfile.template,prefix=osp.basename(output),dir=osp.dirname(output),)
				f = open(tmp_file, "ab")
			else:
				tmp_file = None
				f = output
			if tmp_file is not None and f.tell() != 0:
				headers["Range"] = "bytes={}-".format(f.tell())
				res = sess.get(url, headers=headers, stream=True, verify=verify)
			#if not quiet:
			#	print("Downloading...", file=sys.stderr)
			#	if resume:
			#		print("Resume:", tmp_file, file=sys.stderr)
			#	print("From:", url_origin, file=sys.stderr)
			#	print("To:",osp.abspath(output) if output_is_path else output,file=sys.stderr,)
			try:
				total = res.headers.get("Content-Length")
				if total is not None:
					total = int(total)
				t_start = time.time()
				for chunk in res.iter_content(chunk_size=CHUNK_SIZE):
					f.write(chunk)
					p_count=p_count+len(chunk)
					percent=int((p_count/total)*100)
					self.update_progress.emit([set_id[i][2],percent,p_count])
					if speed is not None:
						elapsed_time_expected = 1.0 * pbar.n / speed
						elapsed_time = time.time() - t_start
						if elapsed_time < elapsed_time_expected:
							time.sleep(elapsed_time_expected - elapsed_time)
				if tmp_file:
					f.close()
					shutil.move(tmp_file, output)
			except IOError as e:
				print(e, file=sys.stderr)
				return
			finally:
				sess.close()
			if dc==len(set_id):
				zerotwo=True
			self.terminal_progress.emit("{yo} has been downloaded".format(yo=set_id[i][1][1:]))
			self.msg_progress.emit(zerotwo)	

global service
global set_id
global fname
global c
c=1
set_id={}

class Res(QMainWindow, Ui_MainWindow):
	def __init__(self,parent = None):
		global progess_total,curr_progress
		super(Res,self).__init__(parent)
		self.setupUi(self)
		self.rect=QRect(200,20,0,501)
		self.rezero.setGeometry(self.rect)
		self.download.setEnabled(False)
		self.clicked=False
		"""item1=self.listid.horizontalHeaderItem(0)
								item1.setForeground(QtGui.QColor(255, 0, 0))
								item1.setBackground(QtGui.QColor(255, 0, 0))
								self.listid.setHorizontalHeaderItem(0,item1)"""
		self.listid.setColumnWidth(0,2)
		self.listid.setColumnWidth(1,240)
		self.listid.setColumnWidth(2,65)
		self.listid.setColumnWidth(3,100)
		self.listid.setColumnWidth(4,90)
		self.listid.setRowCount(1)
		self.listid.setItem(0,1,QtWidgets.QTableWidgetItem("File Name"))
		self.listid.setItem(0,2,QtWidgets.QTableWidgetItem("Type"))
		self.listid.setItem(0,3,QtWidgets.QTableWidgetItem("Size"))
		self.listid.setItem(0,4,QtWidgets.QTableWidgetItem("Progress"))
		#self.listid.setColumnWidth(4,60)
		self.logo.setReadOnly(True)
		self.dirlabel.setReadOnly(True)
		self.getinfo.setEnabled(False)
		#self.dirlabel.setReadOnly(True)
		self.dirchooser.clicked.connect(self.choose_folder)
		self.connect.clicked.connect(self.connect_drive)
		self.exit.clicked.connect(self.exit_st)
		self.connect.setStyleSheet('''
			QPushButton
			{
			background-color: rgb(255, 255, 255);
			font: 75 9pt "Agency FB";
			font-weight: Bold;
			border-radius: 40px;
			}
			QPushButton::hover
			{
			color: white;
			font: 75 10pt "Agency FB";
			font-weight: Bold;
			background-color: qlineargradient(spread:pad, x1:0, y1:0.489, x2:1, y2:0.489, stop:0 rgba(147, 122, 255, 255), stop:0.982955 rgba(255, 171, 171, 255));
			}
			''')
		self.getinfo.clicked.connect(self.drive_info)
		self.download.clicked.connect(self.file_download)

	def exit_st(self):
		exit()

	def file_download(self):
		self.download.setEnabled(False)
		self.dirchooser.setEnabled(False)
		self.worker=WorkerThread()
		self.worker.start()
		self.worker.update_progress.connect(self.update_progress_percent)
		self.worker.terminal_progress.connect(self.update_terminal)
		self.worker.msg_progress.connect(self.msg_box)

	def update_terminal(self,yoyo):
		self.logo.append(" "+yoyo)

	def msg_box(self,val):
		if val==True:
			res=QMessageBox.information(self, "SSup", "Download Completed",QMessageBox.Ok)
			if res==QMessageBox.Ok:
				exit()


	def update_progress_percent(self,val):
		global curr_progress,progess_total
		curr_progress=curr_progress+val[2]
		self.progress.setValue(int((curr_progress/progess_total)*100))
		self.listid.setItem(val[0],4,QtWidgets.QTableWidgetItem(str(val[1])+"%"))
		if int((curr_progress/progess_total)*100)>=100:
			self.progress.setValue(100)
				

	def choose_folder(self):
		global fname
		fname=str(QFileDialog.getExistingDirectory(self, 'Select Directory'))
		self.dirlabel.setText(fname)
		self.download.setEnabled(True)	

	def connect_drive(self):
		global service
		self.connect.setEnabled(False)
		c_file="token.json"
		api_name="drive"
		api_version="v3"
		scope=["https://www.googleapis.com/auth/drive"]

		service=self.Create_Service(c_file,api_name,api_version,scope)
		if service is None:
			self.logo.append(" Connection Failed")
			self.connect.setEnabled(True)
		else:
			self.logo.append(" Connection Made Successfull")
			self.getinfo.setEnabled(True)
			self.anime=QPropertyAnimation(self.rezero,b'geometry')
			self.anime.setDuration(1200)
			self.anime.setStartValue(QRect(200,20,0,501))
			self.anime.setEndValue(QRect(200,20,671,501))
			self.anime.start()

	def get_child(self,query):
		global service
		page_token=None
		result_set=[]
		while True:
			response=service.files().list(q=query,fields='nextPageToken,files(id,name,mimeType,parents,size,fileExtension)',pageToken=page_token).execute()
			result_set.extend(response.get('files'))
			page_token=response.get('nextPageToken',None)
			if page_token is None:
				break
		return result_set

	def recursive_pro(self,ff,path):
		global set_id
		global c
		global service
		global progess_total
		if ff['mimeType']=="application/vnd.google-apps.folder":
			query=f"'{ff['id']}' in parents and trashed=false"
			path=path+"/"+ff['name']
			x=self.get_child(query)
			for i in x:
				self.recursive_pro(i,path)
		else:
			set_id[ff['id']]=[path,"/"+ff['name'],c]
			progess_total=progess_total+int(ff['size'])
			self.listid.setRowCount(c+1)
			self.listid.setItem(c,1,QtWidgets.QTableWidgetItem(ff['name']))
			#self.listid.setItem(c,1,QtWidgets.QTableWidgetItem(ff['id']))
			self.listid.setItem(c,2,QtWidgets.QTableWidgetItem(ff['fileExtension']))
			self.listid.setItem(c,3,QtWidgets.QTableWidgetItem(ff['size']))
			self.listid.setItem(c,4,QtWidgets.QTableWidgetItem("0%"))
			c+=1

	def validate(self,xlink):
		if ("drive.google.com" not in xlink) or ("folders" not in xlink):
			return xlink,False 
		url=xlink[xlink.rfind("/")+1:]
		if "?" in url:
			url=url[:url.rfind("?")]
		return url,True
	def drive_info(self):
		global service
		self.getinfo.setEnabled(False)
		xlink=self.inputid.text()
		link,valid=self.validate(xlink)
		if valid:
			query=f"'{link}' in parents and trashed=false"
			"""response=service.files().list(q=query).execute()
									files=response.get('files')
									nextPageToken=response.get('nextPageToken')
							
									while nextPageToken:
										response=service.files().list(q=query,pageToken=nextPageToken).execute()
										files.extend(response.get('files'))
										nextPageToken=response.get('nextPageToken')
									for i in files:
										print(i)"""
			x=self.get_child(query)
			for i in x:
				self.recursive_pro(i,"Shared_folder")
		else:
			self.getinfo.setEnabled(True)
			self.logo.append(" The URL you have Entered is incorrect!")
			self.logo.append(" Please enter URL which is in this format:")
			self.logo.append(" https://drive.google.com/drive/u/0/folders/1lTc0-egg2f09I3r3PglxNAj8Ho44Bm")
			self.logo.append(" OR")
			self.logo.append(" https://drive.google.com/drive/folders/1lTc0-egg2f09I3r3PglxNAj8Ho44Bm?usp=sharing")
	def Create_Service(self,client_secret_file, api_name, api_version, *scopes):
		CLIENT_SECRET_FILE=client_secret_file
		API_SERVICE_NAME=api_name
		API_VERSION = api_version
		SCOPES = [scope for scope in scopes[0]]
		cred = None
		pickle_file = f'token_{API_SERVICE_NAME}_{API_VERSION}.pickle'
		if os.path.exists(pickle_file):
			with open(pickle_file, 'rb') as token:
				cred=pickle.load(token)
		if not cred or not cred.valid:
			if cred and cred.expired and cred.refresh_token:
				cred.refresh(Request())
			else:
				flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET_FILE, SCOPES)
				cred = flow.run_local_server()
			with open(pickle_file,'wb') as token:
				pickle.dump(cred, token)
		try:
			service = build(API_SERVICE_NAME, API_VERSION, credentials=cred)
			#print(API_SERVICE_NAME, 'service created successfully')
			return service
		except Exception as e:
			#print('Unable to connect.')
			#print(e)
			return None			


app=QApplication(sys.argv)
mainwindow=Res()
widget=QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setWindowFlags(QtCore.Qt.FramelessWindowHint)
widget.setAttribute(QtCore.Qt.WA_TranslucentBackground)
widget.setFixedWidth(887)
widget.setFixedHeight(542)
widget.show()
app.exec_()