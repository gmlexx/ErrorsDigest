# coding: utf-8
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

documents = ["""

					Diadoc.FilterIndex.Impl.LiveIndexReading.LiveIndexTaskReadQueueWorker Diadoc.FilterByDocumentDateIndexHost Will retry request to LiveIndex (null)

					""" ,
"""

					Diadoc.FilterIndex.Impl.LiveIndexReading.LiveIndexTaskReadQueueWorker Diadoc.FilterByStatusTimestampIndexHost Will retry request to LiveIndex (null)

					""" ,
"""

					Diadoc.Registration.Auto.AutoRegistrator Diadoc.KeNotificationIndexHost AutoRegister(userId=e138d98f-f966-47c3-a333-60e3d3c0b740, thumbprint=, timestamp=Ticks: 635495079818480058, DateTime: 2014-10-21 17:06:21Z) user not found (null)

					""" ,
"""

					DiaDoc.WebApp.Views.Shared.KeNotification.KeNotificationController diadoc.web Redirect to DocumentNotification from KE: urn:diadoc:document:89d7a90b-2b34-4356-b527-e1afa094567a/e7ce24e9-6574-41f6-8823-618b69e5195c/e2c138c3-fd42-4af0-b6f6-0c577cd88d28@635472429714767303@47509ad9-892e-4198-a949-44bfe92b5367 (null)

					""" ,
"""

					DiadocCommons.Http.Client.DiadocHttpClusterClient Diadoc.OvermindHost Can't perform request 'GET /users/2d7d6dfb-653c-451c-8ee8-a2233f901fdf' to replica properties https://portal-services.kontur.ru/UsersProps/.

					Body: <null> (null)

					DiadocSys.Net.Http.Client.ReplicaFailedException: The operation has timed out ---> System.Net.WebException: The operation has timed out

					   at System.Net.HttpWebRequest.GetResponse()

					   at DiadocSys.Net.Http.Client.HttpClient.GetResponse(HttpEndPoint endPoint, IHttpRequest request) in c:\cement\diadocsys\_Src\DiadocSys.Net.Http\Client\HttpClient.cs:line 35

					   --- End of inner exception stack trace ---

					   at DiadocSys.Net.Http.Client.HttpClient.GetResponse(HttpEndPoint endPoint, IHttpRequest request) in c:\cement\diadocsys\_Src\DiadocSys.Net.Http\Client\HttpClient.cs:line 49

					   at DiadocSys.Net.Http.Client.HttpClusterClient.TryGetResponse(IHttpRequest request, HttpReplica replica, ICollection`1 errors) in c:\cement\diadocsys\_Src\DiadocSys.Net.Http\Client\HttpClusterClient.cs:line 91

					""" ,
"""

					DDServer.Backend.Communication.InfoSender DDServer.Backend DoPerformIteration() failed in worker InfoSender (null)

					DiadocSys.Net.Http.Client.ReplicaFailedException: The operation has timed out ---> System.Net.WebException: The operation has timed out

					   at System.Net.HttpWebRequest.GetResponse()

					   at DiadocSys.Net.Http.Client.HttpClient.GetResponse(HttpEndPoint endPoint, IHttpRequest request) in d:\BuildAgent\work\diadoc-build\_Src\DiadocSys\DiadocSys.Net.Http\Client\HttpClient.cs:line 32

					   --- End of inner exception stack trace ---

					   at DiadocSys.Net.Http.Client.HttpClient.GetResponse(HttpEndPoint endPoint, IHttpRequest request) in d:\BuildAgent\work\diadoc-build\_Src\DiadocSys\DiadocSys.Net.Http\Client\HttpClient.cs:line 46

					   at DDServer.Backend.Communication.InfoSender.TrySendBytes(Byte[] bytes, String front, String localServerName) in d:\BuildAgent\work\ddserver-backend\Communication\InfoSender.cs:line 62

					   at DDServer.Backend.Communication.InfoSender.DoPerformIteration() in d:\BuildAgent\work\ddserver-backend\Communication\InfoSender.cs:line 47

					   at DiadocSys.Threading.IterativeBackgroundThreadWorker.PerformIteration() in d:\BuildAgent\work\diadoc-build\_Src\DiadocSys\DiadocSys.Threading\IterativeBackgroundThreadWorker.cs:line 70

					""" ,
"""

					DiadocCommons.Http.Client.DiadocHttpClusterClient Diadoc.BillingHandlerHost Can't perform request: Post /Balance/ReceiveTransaction?productId=Diadoc&transactionId=4827f716-d3b1-47ff-8d12-d32a3b2bce2f&senderId=907a3b09-7213-416b-9ea1-9d5f6df810c2&recipientId=8b3ed636-aca5-446a-ab85-ef44ab6ca9d9&resourceId=Invoice&serviceId=exchange&count=1&createDateTicks=635495392467617326&comment=%D1%81%D1%87%D0%B5%D1%82-%D1%84%D0%B0%D0%BA%D1%82%D1%83%D1%80%D0%B0%20%E2%84%9626%26%23160%3B045%20%D0%BE%D1%82%2031.07.14%2C%20%D0%BE%D1%82%D0%BF%D1%80%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%3A%2007.08.14%2011%3A48%20%28%D0%9C%D0%A1%D0%9A%29%2C%20%D1%81%D1%83%D0%BC%D0%BC%D0%B0%3A%207046%2C36%2C%20%D1%81%D1%81%D1%8B%D0%BB%D0%BA%D0%B0%20%D0%BD%D0%B0%20%D0%B4%D0%BE%D0%BA%D1%83%D0%BC%D0%B5%D0%BD%D1%82%3A%20https%3A%2F%2Fdiadoc.kontur.ru%2FShowDocument%3FboxId%3De5c87829-ce14-4537-9468-5903c88c74ce%26messageId%3De36ac74e-8601-437e-9861-c71d618b530c%26entityId%3D4827f716-d3b1-47ff-8d12-d32a3b2bce2f

					Body: <null>

					Exception: DiadocSys.Net.Http.Client.HttpClientException: ResponseStatusCode: InternalServerError

					RequestUrl: https://billy-api.kontur.ru/Balance/ReceiveTransaction?productId=Diadoc&tra…ice&serviceId=exchange&count=1&createDateTicks=635495392467617326&comment=счет-фактура №26%26%23160%3B045 от 31.07.14%2C отправлен: 07.08.14 11:48 (МСК)%2C сумма: 7046%2C36%2C ссылка на документ: https:%2F%2Fdiadoc.kontur.ru%2FShowDocument%3FboxId%3De5c87829-ce14-4537-9468-5903c88c74ce%26messageId%3De36ac74e-8601-437e-9861-c71d618b530c%26entityId%3D4827f716-d3b1-47ff-8d12-d32a3b2bce2f

					<!DOCTYPE html>

					<html>

					    <head>

					        <title>Runtime Error</title>

					        <meta name="viewport" content="width=device-width" />

					        <style>

					         body {font-family:"Verdana";font-weight:normal;font-size: .7em;color:black;}

					         p {font-family:"Verdana";font-weight:normal;color:black;margin-top: -5px}

					         b {font-family:"Verdana";font-weight:bold;color:black;margin-top: -5px}

					         H1 { font-family:"Verdana";font-weight:normal;font-size:18pt;color:red }

					         H2 { font-family:"Verdana";font-weight:normal;font-size:14pt;color:maroon }

					         pre {font-family:"Consolas","Lucida Console",Monospace;font-size:11pt;margin:0;padding:0.5em;line-height:14pt}

					         .marker {font-weight: bold; color: black;text-decoration: none;}

					         .version {color: gray;}

					         .error {margin-bottom: 10px;}

					         .expandable { text-decoration:underline; font-weight:bold; color:navy; cursor:hand; }

					         @media screen and (max-width: 639px) {

					          pre { width: 440px; overflow: auto; white-space: pre-wrap; word-wrap: break-word; }

					         }

					         @media screen and (max-width: 479px) {

					          pre { width: 280px; }

					         }

					        </style>

					    </head>



					    <body bgcolor="white">



					            <span><H1>Server Error in '/' Application.<hr width=100% size=1 color=silver></H1>



					            <h2> <i>Runtime Error</i> </h2></span>



					            <font face="Arial, Helvetica, Geneva, SunSans-Regular, sans-serif ">



					            <b> Description: </b>An application error occurred on the server. The current custom error settings for this application prevent the details of the application error from being viewed remotely (for security reasons). It could, however, be viewed by browsers running on the local server machine.

					            <br><br>



					            <b>Details:</b> To enable the details of this specific error message to be viewable on remote machines, please create a &lt;customErrors&gt; tag within a &quot;web.config&quot; configuration file located in the root directory of the current web application. This &lt;customErrors&gt; tag should then have its &quot;mode&quot; attribute set to &quot;Off&quot;.<br><br>



					            <table width=100% bgcolor="#ffffcc">

					               <tr>

					                  <td>

					                      <code><pre>



					&lt;!-- Web.Config Configuration File --&gt;



					&lt;configuration&gt;

					    &lt;system.web&gt;

					        &lt;customErrors mode=&quot;Off&quot;/&gt;

					    &lt;/system.web&gt;

					&lt;/configuration&gt;</pre></code>



					                  </td>

					               </tr>

					            </table>



					            <br>



					            <b>Notes:</b> The current error page you are seeing can be replaced by a custom error page by modifying the &quot;defaultRedirect&quot; attribute of the application&#39;s &lt;customErrors&gt; configuration tag to point to a custom error page URL.<br><br>



					            <table width=100% bgcolor="#ffffcc">

					               <tr>

					                  <td>

					                      <code><pre>



					&lt;!-- Web.Config Configuration File --&gt;



					&lt;configuration&gt;

					    &lt;system.web&gt;

					        &lt;customErrors mode=&quot;RemoteOnly&quot; defaultRedirect=&quot;mycustompage.htm&quot;/&gt;

					    &lt;/system.web&gt;

					&lt;/configuration&gt;</pre></code>



					                  </td>

					               </tr>

					            </table>



					            <br>



					    </body>

					</html>



					   at DiadocSys.Net.Http.Client.HttpResponseExtensions.CheckStatusCode(IHttpResponse response, HttpStatusCode[] allowedStatusCodes) in c:\cement\diadocsys\_Src\DiadocSys.Net.Http\Client\HttpResponseExtensions.cs:line 23

					   at DiadocSys.Net.Http.Client.HttpClusterClientExtensions.PerformVoidHttpRequest(IHttpClusterClient httpClient, IRequestContext requestContext, String queryString, HttpMethod httpMethod, HttpRequestBody httpRequestBody, Nullable`1 clientId) in c:\cement\diadocsys\_Src\DiadocSys.Net.Http\Client\HttpClusterClientExtensions.cs:line 108 ClientSystemId: kansoTailReader, Authorization: skip, RequestId: f71ccb60-ac0e-4e88-9d01-437bd2061ac8

					""" ,
"""

					Diadoc.Registration.Auto.AutoRegistrator diadoc.webadmin AutoRegister(userId=5d85f5e7-8212-4b36-9025-583f4f9946e5, thumbprint=e84fc19f3a4b410bf4b0486c278158aefe70be28, timestamp=Ticks: 635495474071790395, DateTime: 2014-10-22 04:03:27Z) organization registration skipped: INN in certificate is empty (null)

					""" ,
"""

					Diadoc.Protocols.Portal.PortalAuth.AuthTokenAccessor`1[[Diadoc.Protocols.Portal.PortalAuth.PortalToken, Diadoc.Protocols.Portal, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]] diadoc.web Failed to extract token from: 888jwYrnXRFEU9pnHC8TZouN/OJTdGL0NQV50Niq2fL1uOFVF7vXt7uT3Wo3dZunKG2XrPiZxE5w7tGZ7exU6g== (null)

					System.FormatException: Unrecognized Guid format.

					   at System.Guid.GuidResult.SetFailure(ParseFailureKind failure, String failureMessageID, Object failureMessageFormatArgument, String failureArgumentName, Exception innerException)

					   at System.Guid.TryParseGuid(String g, GuidStyles flags, GuidResult& result)

					   at System.Guid..ctor(String g)

					   at Diadoc.Protocols.Portal.PortalAuth.PortalToken.Deserialize(String input)

					   at Diadoc.Protocols.Portal.PortalAuth.AuthTokenAccessor`1.TryExtractToken(String base64EncodedToken)

					""" ,
"""

					Diadoc.Handlers.EmailNotifier.Impl.EmailSending.EmailSendTaskHandler Diadoc.EmailNotifierHost Email address appears to be userId. Need to resync user info? EmailSenderTask: MessageType: NewEmployeeRequestForAdminEmailTaskData, SendToEmail: 5dfbd5e4-567d-42ce-b603-6ca1e1d01cbb, UserId: b46c9bdb-e898-49cf-9200-e49caa0ac873, MessageByte: 228 bytes ClientSystemId: EmployeeRequestEventEmailSender, Authorization: skip, RequestId: 8401ccf4-679e-4c9c-9cb3-0528de67a8f2

					""" ,
"""

					Diadoc.Organizations.Impl.Registration.OrganizationRegistrator Diadoc.KeNotificationIndexHost Found head organization with another KPP OrgId: a5c01f0e-dbf3-4269-98f1-97e15a2b157d, BoxId: 1f2ea5a0-59e7-4692-8236-e2e974b2d0d2, FnsParticipantId: 2BM-5403195312-540401001-201407010824326256265, Inn: 5403195312, Kpp: 540401001, ShortName: Общество с ограниченной ответственностью "Астрея", Timestamp: Ticks: 635397998720000000, DateTime: 2014-07-01 08:24:32Z, CreationTimestamp: Ticks: 635397854720000000, DateTime: 2014-07-01 04:24:32Z, DeletedTimestamp: , BillingAccountId: 724c9877-7db8-45ea-a14f-6f1695efb9d1, AbonId: , JoinedTimestamp: Ticks: 635397854720000000, DateTime: 2014-07-01 04:24:32Z, FnsRegistrationDate: , FirstActivityTimestamp: , IsBranch: False, IsPilot: False, DelegateGnivcSvcTxs: , Properties: Ogrn: , IfnsCode: , CountryCode: , ForeignAddress: , PostCode: , RegionCode: , Region: , District: , City: , Settlement: , Street: , House: , Building: , FlatOrOffice: , FirstName: , MiddleName: , LastName: , CertificateOfRegistryInfo:  for model: Inn: 5403195312, Kpp: 540301001, FullName: ООО "Астрея", BillingAccountId: f672b849-3093-40a6-916f-b18456c30f70, DealerId: , KeAbonentId:  (null)

					""" ,
"""

					DiaDoc.WebApp.Controllers.Send.NonformalizedAttachmentModelProvider diadoc.web Document recognition error: System.NotSupportedException: Cannot recognize document (invalid format) ---> System.IO.IOException: Invalid header signature; read 0x342E312D46445025, expected 0xE11AB1A1E011CFD0

					   at NPOI.POIFS.Storage.HeaderBlock..ctor(Stream stream)

					   at NPOI.POIFS.FileSystem.POIFSFileSystem..ctor(Stream stream)

					   at NPOI.HSSF.UserModel.HSSFWorkbook..ctor(Stream s, Boolean preserveNodes)

					   at NPOI.HSSF.UserModel.HSSFWorkbook..ctor(Stream s)

					   at FieldsRecognition.DocumentModel.Excel.ExcelModelBuilder..ctor(Stream stream)

					   at FieldsRecognition.DocumentModel.Excel.ExcelModelBuilder.BuilderFrom(Stream stream)

					   --- End of inner exception stack trace ---

					   at FieldsRecognition.DocumentModel.Excel.ExcelModelBuilder.BuilderFrom(Stream stream)

					   at DiaDoc.WebApp.Controllers.Send.NonformalizedAttachmentModelProvider.GetAttachment2Send(Byte[] fileContent, String filename, ClientContentLocation serverSideLocation)

					   at DiaDoc.WebApp.Controllers.Send.NonformalizedAttachmentModelProvider.TryGetAttachment2Send(Byte[] fileContent, String filename, ClientContentLocation serverSideLocation) (null)

					""" ,
"""

					Diadoc.Search.Impl.Update.SearchIndexUpdater Diadoc.SearchIndexHost No documents found for letterKey: 1f06df21-a917-494b-b4e7-035239bd233b_e506b1c9-05b6-4f84-a783-94ed8c80a611 (null)

					""" ,
"""

					Diadoc.Preview.Impl.PreviewTaskPipelineFactory Diadoc.PreviewHost Task Diadoc.Preview.PreviewTask, ERROR: Code: , UserMessage: Файл такого типа не поддерживается., ApiClientMessage: , SystemMessage: {"Source":{"FileOnShelf":null,"KansoLocation":{"FileNumber":5,"Offset":361359310904,"Key":"cf64062e-5385-11e4-8000-623fa3913099","TotalSize":13639},"Filename":"Счет (аванс)_12925070_20141010.htm"},"PageRange":{"FromPage":0,"ToPage":9},"OutputFormat":1,"Resolution":120,"TargetDirOnShelf":"/preview/5_361359310904_dpi120","PageId":null}, Data: , Timestamp: Ticks: 635495406322351892, DateTime: 2014-10-22 02:10:32Z, Hidden: False RequestId: 99315c9b-9df7-479d-b03e-52b48121b1d7, Thumbprint: efc94ba062142cc88d6f21f022d4cd7944ba1a1d, ClientSystemId: diadoc.web, Locale: ru, SessionId: 00000000-0000-0000-0000-000000000000

					df225275-211b-4479-9d48-84ed7361a743

					efc94ba062142cc88d6f21f022d4cd7944ba1a1d

					635495406186938077

					0

					755222DF1B2179449D4884ED7361A743A6B312EE9DD8654A8D0CC72AE1DFEE30, UserId: df225275-211b-4479-9d48-84ed7361a743, PreviewID: 3c37141a-3601-4490-9867-69332c9f4e50

					""" ,
"""

					Diadoc.Registration.Auto.AutoRegistrator Diadoc.OvermindHost AutoRegister(userId=b7b96e7b-ff04-42ba-81d8-5773b2915cff, thumbprint=B835ED030524ED8AFEE234211DC764EF1E5A4545, timestamp=Ticks: 635495079584144816, DateTime: 2014-10-21 17:05:58Z) organization registration skipped: certificate is not qualified (null)

					""" ,
"""

					Diadoc.TimeStampServer.Impl.CrlManagement.CrlDownloader Diadoc.TimeStampServerHost Failed to get crl from: http://crl1.rshb.ru/cdp/3568B4067CA0026D05E42789D3C9D72F8136C9C8.crl (null)

					DiadocSys.Net.Http.Client.ReplicaFailedException: The operation has timed out ---> System.Net.WebException: The operation has timed out

					   at System.Net.HttpWebRequest.GetResponse()

					   at DiadocSys.Net.Http.Client.HttpClient.GetResponse(HttpEndPoint endPoint, IHttpRequest request) in c:\cement\diadocsys\_Src\DiadocSys.Net.Http\Client\HttpClient.cs:line 35

					   --- End of inner exception stack trace ---

					   at DiadocSys.Net.Http.Client.HttpClient.GetResponse(HttpEndPoint endPoint, IHttpRequest request) in c:\cement\diadocsys\_Src\DiadocSys.Net.Http\Client\HttpClient.cs:line 49

					   at Diadoc.TimeStampServer.Impl.CrlManagement.CrlDownloader.TryGetCrl(IRequestContext context, String cdpUrl) in c:\cement\diadoc\_Src\App\Diadoc.TimeStampServer.Impl\CrlManagement\CrlDownloader.cs:line 45

					""" ,
"""

					Diadoc.FnsClaim.ClientImpl.Storage.Database.ClaimedDocumentDatabaseCluster Diadoc.FnsClaimHost Can not check replica state 'Server=dd14;Database=diadoc;Uid=claim;Pwd="Bcnht,jdfybzCenmDtotq";Unicode=True;Validate Connection=True;Default Command Timeout=30;Connection Timeout=5' (null)

					BLToolkit.Data.DataException: Can't connect to MySQL server on 'dd14' (10061): Authentication failed. ---> Devart.Data.MySql.MySqlException: Can't connect to MySQL server on 'dd14' (10061): Authentication failed. ---> System.IO.IOException: Unable to read data from the transport connection: An established connection was aborted by the software in your host machine. ---> System.Net.Sockets.SocketException: An established connection was aborted by the software in your host machine

					   at System.Net.Sockets.NetworkStream.Read(Byte[] buffer, Int32 offset, Int32 size)

					   --- End of inner exception stack trace ---

					   at Devart.Common.ad.a(Byte[] A_0, Int32 A_1, Int32 A_2)

					   at Devart.Common.w.c(Byte[] A_0, Int32 A_1, Int32 A_2)

					   at Devart.Common.ae.d(Byte[] A_0, Int32 A_1, Int32 A_2)

					   --- End of inner exception stack trace ---

					   at Devart.Data.MySql.u.a(String A_0, String A_1, String A_2, String A_3, Int32 A_4, String A_5, Int32 A_6, Int32 A_7)

					   at Devart.Data.MySql.j.a(MySqlConnection A_0, String A_1, String A_2, String A_3, String A_4, Int32 A_5, Int32 A_6, MySqlProtocol A_7, Boolean A_8, Boolean A_9)

					   at Devart.Data.MySql.m.a(DbConnectionOptions A_0, Object A_1, DbConnectionBase A_2)

					   at Devart.Common.DbConnectionFactory.a(DbConnectionPool A_0, DbConnectionOptions A_1, DbConnectionBase A_2)

					   at Devart.Common.DbConnectionPool.a(DbConnectionBase A_0)

					   at Devart.Common.DbConnectionPool.GetObject(DbConnectionBase owningConnection)

					   at Devart.Common.DbConnectionFactory.b(DbConnectionBase A_0)

					   at Devart.Common.DbConnectionClosed.Open(DbConnectionBase outerConnection)

					   at Devart.Common.DbConnectionBase.Open()

					   at Devart.Data.MySql.MySqlConnection.j()

					   at BLToolkit.Data.DbManager.ExecuteOperation(OperationType operationType, Action operation) in e:\Work\dev\.net\bltoolkit\Source\Data\DbManager.cs:line 4420

					   --- End of inner exception stack trace ---

					   at BLToolkit.Data.DbManager.OnOperationException(OperationType op, DataException ex) in e:\Work\dev\.net\bltoolkit\Source\Data\DbManager.cs:line 611

					   at BLToolkit.Data.DbManager.HandleOperationException(OperationType op, Exception ex) in e:\Work\dev\.net\bltoolkit\Source\Data\DbManager.cs:line 4459

					   at BLToolkit.Data.DbManager.ExecuteOperation(OperationType operationType, Action operation) in e:\Work\dev\.net\bltoolkit\Source\Data\DbManager.cs:line 4425

					   at BLToolkit.Data.DbManager.OpenConnection() in e:\Work\dev\.net\bltoolkit\Source\Data\DbManager.cs:line 216

					   at BLToolkit.Data.DbManager.get_Connection() in e:\Work\dev\.net\bltoolkit\Source\Data\DbManager.cs:line 191

					   at BLToolkit.Data.DbManager.OnInitCommand(IDbCommand command) in e:\Work\dev\.net\bltoolkit\Source\Data\DbManager.cs:line 482

					   at BLToolkit.Data.DbManager.get_SelectCommand() in e:\Work\dev\.net\bltoolkit\Source\Data\DbManager.cs:line 419

					   at BLToolkit.Data.DbManager.GetCommand(CommandAction commandAction) in e:\Work\dev\.net\bltoolkit\Source\Data\DbManager.cs:line 1917

					   at BLToolkit.Data.DbManager.GetCommand(CommandAction commandAction, CommandType commandType) in e:\Work\dev\.net\bltoolkit\Source\Data\DbManager.cs:line 1949

					   at BLToolkit.Data.DbManager.GetCommand(CommandAction commandAction, CommandType commandType, String sql) in e:\Work\dev\.net\bltoolkit\Source\Data\DbManager.cs:line 513

					   at BLToolkit.Data.DbManager.PrepareCommand(CommandAction commandAction, CommandType commandType, String commandText, IDbDataParameter[] commandParameters) in e:\Work\dev\.net\bltoolkit\Source\Data\DbManager.cs:line 2304

					   at BLToolkit.Data.DbManager.SetCommand(CommandAction commandAction, CommandType commandType, String commandText, IDbDataParameter[] commandParameters) in e:\Work\dev\.net\bltoolkit\Source\Data\DbManager.cs:line 1988

					   at BLToolkit.Data.DbManager.SetCommand(String commandText) in e:\Work\dev\.net\bltoolkit\Source\Data\DbManager.cs:line 2028

					   at DiadocSys.Net.MySql.MySql.MySqlReplicaStateProvider.IsSlaveOk(String connectionString) in c:\cement\diadocsys\_Src\DiadocSys.Net.MySql\MySql\MySqlReplicaStateProvider.cs:line 64

					""" ,
"""

					Diadoc.TimeStampServer.Impl.CrlManagement.CrlDownloader Diadoc.TimeStampServerHost Failed to get crl from: http://ca.orbitacom.ru/cdp/B8500C7AF92D1A2042775CB0479AC6E2107DD23B.crl (null)

					DiadocSys.Net.Http.Client.HttpClientException: ResponseStatusCode: NotFound

					RequestUrl: http://ca.orbitacom.ru/cdp/B8500C7AF92D1A2042775CB0479AC6E2107DD23B.crl

					<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">

					<HTML><HEAD><TITLE>?? ??????? ????? ????????? ????????</TITLE>

					<META HTTP-EQUIV="Content-Type" Content="text/html; charset=windows-1251">

					<STYLE type="text/css">

					  BODY { font: 8pt/12pt verdana }

					  H1 { font: 13pt/15pt verdana }

					  H2 { font: 8pt/12pt verdana }

					  A:link { color: red }

					  A:visited { color: maroon }

					</STYLE>

					</HEAD><BODY><TABLE width=500 border=0 cellspacing=10><TR><TD>



					<h1>?? ??????? ????? ????????? ????????</h1>

					??????????? ???????? ???????, ????????????? ??? ???????? ??????????.

					<hr>

					<p>?????????? ????????? ?????????.</p>

					<ul>

					<li>?????????, ??? ????????????  ? ???????? ?????? ???????????? ????? ???-???? ??????? ????????? ? ?? ???????? ?????? ??????????????.</li>

					<li>???? ?? ?????? ?? ??? ????????, ?????? ??????, ?? ????????? ? ??????????????? ???-???? ? ???????????? ??? ? ??????????? ??????????????? ??????.

					</li>

					<li>??????? ?????? <a href="javascript:history.back(1)">?????</a>, ????? ????????? ?????? ??????.</li>

					</ul>

					<h2>HTTP Error 404 - File or directory not found.<br>Internet Information Services (IIS)</h2>

					<hr>

					<p>??????????? ???????? (??? ??????????? ?????? ?????????)</p>

					<ul>

					<li>????????? ????? ?? ???????? ?????? <b>HTTP</b> ? <b>404</b> ?? <a href="http://go.microsoft.com/fwlink/?linkid=8180">???-???? ??????????? ????????? ?????????? Microsoft</a>.</li>

					<li>??????? ??????? ??? ????????? <b>????????? ???-????</b>, <b>??????? ????? ?????????????????</b> ? <b>? ??????????? ?????????? ?? ???????</b>, ??????? ?????????? ? <b>??????? IIS</b>. <b>??????? IIS</b> ???????? ? ????????? ?????????? IIS? (inetmgr).  </li>

					</ul>



					</TD></TR></TABLE></BODY></HTML>



					   at DiadocSys.Net.Http.Client.HttpResponseExtensions.CheckStatusCode(IHttpResponse response, HttpStatusCode[] allowedStatusCodes) in c:\cement\diadocsys\_Src\DiadocSys.Net.Http\Client\HttpResponseExtensions.cs:line 23

					   at Diadoc.TimeStampServer.Impl.CrlManagement.CrlDownloader.TryGetCrl(IRequestContext context, String cdpUrl) in c:\cement\diadoc\_Src\App\Diadoc.TimeStampServer.Impl\CrlManagement\CrlDownloader.cs:line 45

					""" ,
"""

					Diadoc.Handlers.FnsReg.Impl.FnsRegMessageHandler Diadoc.FnsRegHost Duplicate task detected: {"FakeDocflowId":"9010fcfe-564e-4aac-b78c-2cf8757b26db","FnsParticipantId":"2BM-7203243989-2012052808110961422630000000000","FnsRegistrationDate":"21.10.2014","Organization":{"Name":"Общество с ограниченной ответственностью \"Эталон\"","Inn":"7203243989","Kpp":"720301001","Ogrn":"1107232001161","TaxInspCode":"7203","Address":{"ZipCode":"625007","Region":"72","Territory":null,"City":"Тюмень","Locality":null,"Street":"ул Широтная","Building":"27","Block":"1","Apartment":null}},"Certificates":[{"BeginDate":"27.01.2014","EndDate":"27.01.2015","Certificate":"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"}]} RequestId: b211ab2a-be40-4369-8ea6-e4ea1ceb1b09, Thumbprint: 5126ef165ba6433c6a88803e297d76537e536456, ClientSystemId: diadoc.web, Locale: ru, SessionId: 00000000-0000-0000-0000-000000000000

					240bb26c-95ba-4329-b7dc-53f5dc2e2607

					5126ef165ba6433c6a88803e297d76537e536456

					635495087630450299

					0

					6CB20B24BA952943B7DC53F5DC2E2607A6E77A16FE8C1B4A9C1C4968E5A53093, UserId: 240bb26c-95ba-4329-b7dc-53f5dc2e2607

					""" ,
"""

					DiadocCommons.Http.Server.DiadocHttpServer Diadoc.OvermindHost Could not flush response body. Request: SessionId: 5c2abb74-c62c-4f2c-9351-1a7c08160c77

					49675b7f-3d0b-4ab9-92ab-a317afacfe28

					6588D9ED71ADF63CF64C8908EE923BE8668F2F01

					635495079185653352

					0

					, UserId: 49675b7f-3d0b-4ab9-92ab-a317afacfe28, ClientSystemId: diadoc.api:mariaRa-1c-b9122233-7941-47a5-908c-dfe8a10fc480, Thumbprint: 6588D9ED71ADF63CF64C8908EE923BE8668F2F01, RequestId: 832508bd-78e8-472b-b3e2-5824c5159093 (null)

					System.Net.HttpListenerException (0x80004005): The specified network name is no longer available

					   at System.Net.HttpResponseStream.Write(Byte[] buffer, Int32 offset, Int32 size)

					   at DiadocSys.Net.Http.Server.HttpContext.SafeFlushResponseBody() in c:\cement\diadocsys\_Src\DiadocSys.Net.Http\Server\HttpContext.cs:line 249

					""" ,
"""

					Diadoc.TimeStampServer.Impl.CrlManagement.CrlDownloader Diadoc.TimeStampServerHost Failed to get crl from: http://atlas.atnn.ru/crl/e1d147891f686924b88089dbca43641da3a51cae.crl (null)

					DiadocSys.Net.Http.Client.HttpClientException: ResponseStatusCode: NotFound

					RequestUrl: http://atlas.atnn.ru/crl/e1d147891f686924b88089dbca43641da3a51cae.crl

					<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">

					<html><head>

					<title>404 Not Found</title>

					</head><body>

					<h1>Not Found</h1>

					<p>The requested URL /crl/e1d147891f686924b88089dbca43641da3a51cae.crl was not found on this server.</p>

					<hr>

					<address>Apache/2.2.22 (Debian) Server at atlas.atnn.ru Port 80</address>

					</body></html>



					   at DiadocSys.Net.Http.Client.HttpResponseExtensions.CheckStatusCode(IHttpResponse response, HttpStatusCode[] allowedStatusCodes) in c:\cement\diadocsys\_Src\DiadocSys.Net.Http\Client\HttpResponseExtensions.cs:line 23

					   at Diadoc.TimeStampServer.Impl.CrlManagement.CrlDownloader.TryGetCrl(IRequestContext context, String cdpUrl) in c:\cement\diadoc\_Src\App\Diadoc.TimeStampServer.Impl\CrlManagement\CrlDownloader.cs:line 45

					""" ,
"""

					Diadoc.Roaming.Impl.BoxWatcher.BoxReader Diadoc.Roaming.RoamingBoxWatcherHost Failed to update watcher (boxId: 1f29602d-db95-41af-9827-a38ecc91dee4, messageId: , eventId: ): Diadoc.Api.Http.HttpClientException: BaseUrl=https://diadoc-api.kontur.ru, PathAndQuery=/V4/GetNewEvents?includeDrafts&boxId=1f29602d-db95-41af-9827-a38ecc91dee4, AdditionalMessage=Access to Box 1f29602d-db95-41af-9827-a38ecc91dee4 is denied, StatusCode=Forbidden ---> System.Net.WebException: The remote server returned an error: (403) Forbidden.

					   at System.Net.HttpWebRequest.GetResponse()

					   at Diadoc.Api.Http.HttpClient.PerformHttpRequest(HttpRequest request, HttpStatusCode[] allowedStatusCodes) in c:\dev\diadocsdk\C#\DiadocApi\Http\HttpClient.cs:line 93

					   --- End of inner exception stack trace ---

					   at Diadoc.Api.Http.HttpClient.PerformHttpRequest(HttpRequest request, HttpStatusCode[] allowedStatusCodes) in c:\dev\diadocsdk\C#\DiadocApi\Http\HttpClient.cs:line 120

					   at Diadoc.Api.DiadocHttpApi.PerformHttpRequest[TResponse](String token, String method, String queryString, Byte[] requestBody, Func`2 convertResponse, String errorMessage) in c:\dev\diadocsdk\C#\DiadocApi\DiadocHttpApi.cs:line 60

					   at Diadoc.Api.DiadocHttpApi.PerformHttpRequest[TResponse](String token, String method, String queryString, Byte[] requestBody) in c:\dev\diadocsdk\C#\DiadocApi\DiadocHttpApi.cs:line 49

					   at Diadoc.Api.DiadocHttpApi.GetNewEvents(String authToken, String boxId, String afterEventId) in c:\dev\diadocsdk\C#\DiadocApi\DiadocHttpApi.Events.cs:line 15

					   at Diadoc.Roaming.Impl.Common.DiadocInterop.DiadocApiClient.GetNewEvents(String boxId, String lastEventId) in c:\cement\diadoc\_Src\Roaming\Diadoc.Roaming.Impl\Common\DiadocInterop\DiadocApiClient.cs:line 44

					   at Diadoc.Roaming.Impl.BoxWatcher.BoxReader.GetNewBoxEvents(String lastEventId) in c:\cement\diadoc\_Src\Roaming\Diadoc.Roaming.Impl\BoxWatcher\BoxReader.cs:line 86

					   at Diadoc.Roaming.Impl.BoxWatcher.BoxReader.ReadNewEvents() in c:\cement\diadoc\_Src\Roaming\Diadoc.Roaming.Impl\BoxWatcher\BoxReader.cs:line 55 (null)

					""" ,
"""

					Diadoc.Web.Commons.HttpApplicationBase diadoc.web Unhandled exception. RequestId: 409b76ad-c275-484d-baad-4aecbd73094a, Thumbprint: 95537d3195d381c4ceb5a7a363e00572d4ebb0c0, ClientSystemId: diadoc.web, Locale: ru, SessionId: 00000000-0000-0000-0000-000000000000

					eb028732-684e-4215-a2b5-0b411b8176d7

					95537d3195d381c4ceb5a7a363e00572d4ebb0c0

					635491309901279336

					0

					328702EB4E681542A2B50B411B8176D7C174A196C7D6A94DAB51E1BF56F51562, UserId: eb028732-684e-4215-a2b5-0b411b8176d7, Url: http://diadoc.kontur.ru/844b9d1f-36e6-40e9-94a3-ee78d41e665b/Folder/GetPendingCount?_=1413911719230 (null)

					System.Reflection.TargetInvocationException: Exception has been thrown by the target of an invocation. ---> System.AggregateException: One or more errors occurred. ---> System.IndexOutOfRangeException: Index was outside the bounds of the array.

					   at System.Collections.Generic.Dictionary`2.Insert(TKey key, TValue value, Boolean add)

					   at DiadocSys.Net.Context.RequestContextData.SetGuid(String key, Nullable`1 value)

					   at DiadocSys.Net.Context.RequestContext.get_RequestId()

					   at DiadocMonitoring.Profiling.Profiler.Profile(IRequestContext requestContext, String target, String requestUrl, Timestamp startTimestamp, TimeSpan elapsedTime, Boolean failed, Boolean isSubRequest, Boolean aborted)

					   at DiadocCommons.Redis.DiadocRedisClusterClient.<>c__DisplayClass2.<.ctor>b__0(RequestCompletedEventArgs args)

					   at System.Action`1.Invoke(T obj)

					   at DiadocSys.Net.Redis.RedisClusterClient.ExecuteRequestActionTask[TResult](IRequestContext requestContext, Task`1 task, Replica replica)

					   at DiadocSys.Net.Redis.RedisClusterClient.<>c__DisplayClass24`1.<GetReplicaTask>b__23()

					   at System.Threading.Tasks.Task`1.InnerInvoke()

					   at System.Threading.Tasks.Task.Execute()

					   --- End of inner exception stack trace ---

					   at System.Threading.Tasks.Task.WaitAll(Task[] tasks, Int32 millisecondsTimeout, CancellationToken cancellationToken)

					   at DiadocSys.Net.Redis.RedisClusterClient.PerformWriteRequest(IRequestContext requestContext, Func`2 requestAction)

					   at DiadocSys.Net.Redis.RedisClusterClient.HashSet(IRequestContext requestContext, String key, Dictionary`2 values, DateTime expireAt)

					   at Diadoc.Web.Sessions.Session.FlushChanges()

					   at Diadoc.Web.Sessions.Session.UpdateChanges()

					   at Diadoc.Web.Commons.HttpApplicationBase.Application_EndRequest()

					   --- End of inner exception stack trace ---

					   at System.RuntimeMethodHandle.InvokeMethod(Object target, Object[] arguments, Signature sig, Boolean constructor)

					   at System.Reflection.RuntimeMethodInfo.UnsafeInvokeInternal(Object obj, Object[] parameters, Object[] arguments)

					   at System.Reflection.RuntimeMethodInfo.Invoke(Object obj, BindingFlags invokeAttr, Binder binder, Object[] parameters, CultureInfo culture)

					   at System.Reflection.MethodBase.Invoke(Object obj, Object[] parameters)

					   at System.Web.Util.ArglessEventHandlerProxy.Callback(Object sender, EventArgs e)

					   at System.Web.HttpApplication.SyncEventExecutionStep.System.Web.HttpApplication.IExecutionStep.Execute()

					   at System.Web.HttpApplication.ExecuteStep(IExecutionStep step, Boolean& completedSynchronously)

					""" ,
"""

					Diadoc.FnsRegMessagesWatcher.Impl.FnsRegMessagesWatcher Diadoc.FnsRegMessagesWatcherHost FnsRegMessage for participant 2BM-2221213956-222101001-201410200304567373390 with docflowId A1A7B706F38F8E47B287F6BCB2C51B92 is processing for more than 48 hours (null)

					""" ,
"""

					DiaDoc.WebApp.Controllers.Document.DocumentController diadoc.web Сущность уже подписана letterId=3faec9ca-87c8-4cdf-a26b-a894cebb0fa8, entityId=e089fe5a-1351-4098-9595-dbaa91351368 (null)

					""" ,
"""

					DiadocCommons.Http.Server.DiadocHttpServer Diadoc.OvermindHost Client has timed out and therefore request was aborted: Ticks: 635495169295534097, DateTime: 2014-10-21 19:35:29Z 1383 74e8e867-d7ec-48c9-8a70-764cd49f40f3 http://192.168.52.5:27183/ping 192.168.52.5:30117 (null)

					""" ,
"""

					Diadoc.Web.Commons.HttpApplicationBase diadoc.web Unhandled exception. RequestId: 8662428d-542a-4950-ad90-379ebe925d5a, ClientSystemId: diadoc.web, Locale: ru, SessionId: 00000000-0000-0000-0000-000000000000

					b63bdd9f-af89-4b3d-ab8f-fa5a9f315672



					635495498309451300

					0

					, UserId: b63bdd9f-af89-4b3d-ab8f-fa5a9f315672, Url: http://diadoc.kontur.ru/1f4fbe54-a8a1-4ba7-b6d5-7860b4f5efbf/Document/Show?letterId=d20ef7bc-0844-4e4c-9378-40ebe29945c5 (null)

					System.ArgumentException: The parameters dictionary contains a null entry for parameter 'documentId' of non-nullable type 'System.Guid' for method 'System.Web.Mvc.ActionResult Show(System.Guid, System.Guid)' in 'DiaDoc.WebApp.Controllers.Document.DocumentController'. An optional parameter must be a reference type, a nullable type, or be declared as an optional parameter.

					Parameter name: parameters

					   at System.Web.Mvc.ActionDescriptor.ExtractParameterFromDictionary(ParameterInfo parameterInfo, IDictionary`2 parameters, MethodInfo methodInfo)

					   at System.Linq.Enumerable.WhereSelectArrayIterator`2.MoveNext()

					   at System.Linq.Buffer`1..ctor(IEnumerable`1 source)

					   at System.Linq.Enumerable.ToArray[TSource](IEnumerable`1 source)

					   at System.Web.Mvc.ReflectedActionDescriptor.Execute(ControllerContext controllerContext, IDictionary`2 parameters)

					   at System.Web.Mvc.ControllerActionInvoker.InvokeActionMethod(ControllerContext controllerContext, ActionDescriptor actionDescriptor, IDictionary`2 parameters)

					   at System.Web.Mvc.ControllerActionInvoker.<>c__DisplayClass15.<InvokeActionMethodWithFilters>b__12()

					   at System.Web.Mvc.ControllerActionInvoker.InvokeActionMethodFilter(IActionFilter filter, ActionExecutingContext preContext, Func`1 continuation)

					   at System.Web.Mvc.ControllerActionInvoker.InvokeActionMethodFilter(IActionFilter filter, ActionExecutingContext preContext, Func`1 continuation)

					   at System.Web.Mvc.ControllerActionInvoker.InvokeActionMethodWithFilters(ControllerContext controllerContext, IList`1 filters, ActionDescriptor actionDescriptor, IDictionary`2 parameters)

					   at System.Web.Mvc.ControllerActionInvoker.InvokeAction(ControllerContext controllerContext, String actionName)

					   at System.Web.Mvc.Controller.ExecuteCore()

					   at System.Web.Mvc.ControllerBase.Execute(RequestContext requestContext)

					   at System.Web.Mvc.MvcHandler.<>c__DisplayClass6.<>c__DisplayClassb.<BeginProcessRequest>b__5()

					   at System.Web.Mvc.Async.AsyncResultWrapper.<>c__DisplayClass1.<MakeVoidDelegate>b__0()

					   at System.Web.HttpApplication.CallHandlerExecutionStep.System.Web.HttpApplication.IExecutionStep.Execute()

					   at System.Web.HttpApplication.ExecuteStep(IExecutionStep step, Boolean& completedSynchronously)

					""" ,
"""

					Diadoc.Billing.Impl.Abonents.BillingWatcher Diadoc.BillingWatcherHost Error processing billing account OrgInfo: Inn: 7804139630, Kpp: 785050001, FullName: Общество с ограниченной ответственностью "Элис", AccountId: 36d3dd0f-dad9-4849-88b1-b331bdd9e8ff, KeAbonentId: , Timestamp: 999877622: System.InvalidOperationException: Found 2 organizations for billingAccountId: 36d3dd0f-dad9-4849-88b1-b331bdd9e8ff

					   at Diadoc.Organizations.OrganizationFinderExtensions.FindOrganizationByBillingAccountId(IOrganizationFinder organizationFinder, IRequestContext requestContext, Guid billingAccountId) in c:\cement\diadoc\_Src\Organizations\Organizations\OrganizationFinderExtensions.cs:line 49

					   at Diadoc.Organizations.Impl.Registration.OrganizationRegistrator.TryRegisterOrganization(IRequestContext requestContext, OrganizationModel model, Timestamp timestamp) in c:\cement\diadoc\_Src\Organizations\Organizations.Impl\Registration\OrganizationRegistrator.cs:line 120

					   at Diadoc.Billing.Impl.Abonents.BillingWatcher.ProcessItemSafe(BillingAccount account) in c:\cement\diadoc\_Src\Billing\Diadoc.Billing\Impl\Abonents\BillingWatcher.cs:line 50 (null)

					""" ,
"""

					DiadocCommons.Portal.Auth.AuthServiceClient Diadoc.OvermindHost auth error from replica https://portal-services.kontur.ru/auth/auth/password?login=valentyn.kalenichenko@masterdata.ru (null)

					""" ,
"""

					DiadocCommons.Redis.DiadocRedisClusterClient Diadoc.OrganizationsDomainHost BookSleeve.RedisConnection error. EndPoint: 192.168.52.29:6379, Cause: receive (null)

					System.Net.Sockets.SocketException (0x80004005): A request to send or receive data was disallowed because the socket had already been shut down in that direction with a previous shutdown call

					   at BookSleeve.RedisConnectionBase.AsyncReadCompleted(Object sender, SocketAsyncEventArgs e) in d:\Dev\BookSleeve\BookSleeve\RedisConnectionBase.cs:line 659

					""" ,
"""

					Diadoc.TimeStampServer.Impl.SignatureService.SignatureService Diadoc.TimeStampServerHost Some CA certificate in the chain is not valid for the reason UntrustedRoot. Certificate: https://diadoc.kontur.ru/Certificate/Check?base64Cert=MIIFSjCCBPmgAwIBAgIKX…S1upwh8ewvEbCBTLhw7I2f6i37cFXrkCvZa2Ap5H7HBAedvLdMkTmiyUtaKod7rjYF9jq44%3D (null)

					""" ,
"""

					Diadoc.TimeStampServer.Impl.SignatureService.SignatureService Diadoc.TimeStampServerHost Certificate is not trusted with suspicious reason UntrustedRoot, RevocationStatusUnknown, OfflineRevocation. Certificate: https://diadoc.kontur.ru/Certificate/Check?base64Cert=MIIFSjCCBPmgAwIBAgIKX…S1upwh8ewvEbCBTLhw7I2f6i37cFXrkCvZa2Ap5H7HBAedvLdMkTmiyUtaKod7rjYF9jq44%3D (null)

					""" ,
"""

					DiadocCommons.Http.Client.DiadocHttpClusterClient Diadoc.CloudCryptHost Can't perform request 'POST /Groups/FindOrRegister?productId=Diadoc&inn=8615001765&kpp=862201001&name=Общество с ограниченной ответственностью "Арника"' to replica billing2013 https://billy-api.kontur.ru/.

					Body: <empty> (null)

					DiadocSys.Net.Http.Client.ReplicaFailedException: The operation has timed out ---> System.Net.WebException: The operation has timed out

					   at System.Net.HttpWebRequest.GetRequestStream(TransportContext& context)

					   at System.Net.HttpWebRequest.GetRequestStream()

					   at DiadocSys.Net.Http.Client.HttpClient.PrepareWebRequest(IHttpRequest request, Uri uri) in c:\cement\diadocsys\_Src\DiadocSys.Net.Http\Client\HttpClient.cs:line 92

					   at DiadocSys.Net.Http.Client.HttpClient.GetResponse(HttpEndPoint endPoint, IHttpRequest request) in c:\cement\diadocsys\_Src\DiadocSys.Net.Http\Client\HttpClient.cs:line 34

					   --- End of inner exception stack trace ---

					   at DiadocSys.Net.Http.Client.HttpClient.GetResponse(HttpEndPoint endPoint, IHttpRequest request) in c:\cement\diadocsys\_Src\DiadocSys.Net.Http\Client\HttpClient.cs:line 49

					   at DiadocSys.Net.Http.Client.HttpClusterClient.TryGetResponse(IHttpRequest request, HttpReplica replica, ICollection`1 errors) in c:\cement\diadocsys\_Src\DiadocSys.Net.Http\Client\HttpClusterClient.cs:line 91

					""" ,
"""

					Diadoc.TimeStampServer.Impl.CrlManagement.CrlCache Diadoc.TimeStampServerHost Crl doesn't have NextUpdate timestamp: http://ca.skbkontur.ru/cdp/kontur-k2-2008.crl (null)

					""" ,
"""

					DiadocSys.Storage.Framework.EventHandlerHost`1[[Diadoc.UserService.Impl.EmployeeRequests.EmployeeRequestEvent, Diadoc.UserService.Impl, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]] Diadoc.EmployeeRequestEventsHost Failed to handle Event Timestamp: Ticks: 635495252251757210, DateTime: 2014-10-21 21:53:45Z, EventType: RequestSent, AfterEventSnapshot: Id: 92f97b21-783b-433c-8858-4321a937cba3, Timestamp: Ticks: 635495252251757210, DateTime: 2014-10-21 21:53:45Z, OrgId: f7d56947-16fd-4a27-bf03-ea3fbebd91d3, UserId: b46c9bdb-e898-49cf-9200-e49caa0ac873, UserComment: , ApprovalInfo: , RejectionInfo: , EmployeeWasDeleted: False, CertThumbprint: 4de0f5033902f6d34db9dc351ceec96353d4c2f1, AdminComment: , Status: Pending, RequestId: 92f97b21-783b-433c-8858-4321a937cba3 from offset 24695768 by handler Diadoc.UserService.Impl.EmployeeRequests.EmployeeRequestEventEmailSender exception

					System.Exception: Employee request 92f97b21-783b-433c-8858-4321a937cba3 not found

					   at Diadoc.UserService.Impl.EmployeeRequests.EmployeeRequestEventEmailSender.Handle(EmployeeRequestEvent e) in c:\cement\diadoc\_Src\UserService\Diadoc.UserService.Impl\EmployeeRequests\EmployeeRequestEventEmailSender.cs:line 58

					   at DiadocSys.Storage.Framework.EventHandlerHost`1.ProcessEvent(IEntityEventHandler`1 handler, ObjectEventRecord`1 eventRecord) in c:\cement\diadoc\_Src\DiadocSys\DiadocSys.Storage\Framework\EventHandlerHost.cs:line 64 (null)

					""" ,
"""

					Diadoc.Handlers.Recognition.Impl.ToRecognizeHandler Diadoc.RecognitionHost Invalid recognized invoice b629d19c-4e99-4fd4-a639-905721804621. Validation result: IsValid: False, IsValidXml: True, ErrorMessage: Validation error: The required attribute 'ИННЮЛ' is missing.

					, Exception:  (null)

					""" ,
"""

					Diadoc.Handlers.Recognition.Impl.ToRecognizeHandler Diadoc.RecognitionHost Invalid recognized invoice da03d643-93f1-485a-86b2-623728457c5f. Validation result: IsValid: False, IsValidXml: True, ErrorMessage: Validation error: The required attribute 'ИдОтпр' is missing.

					Validation error: The required attribute 'ИдПок' is missing.

					Validation error: The required attribute 'ДатаПРД' is missing.

					Validation error: The required attribute 'ИННЮЛ' is missing.

					, Exception:  (null)

					""" ,
"""

					Diadoc.Web.Commons.HttpApplicationBase diadoc.web Unhandled exception. RequestId: f230e405-96d8-43f7-9e0d-46bcaa5bdd03, ShelfUserId: e4e8ade0-a0d9-4a6d-8c1e-f1a02c953098, ClientSystemId: diadoc.web, Locale: ru, Url: http://diadoc.kontur.ru/48b1368c-bfd7-4394-a32e-14910b14f463/Folder/GetPendingCount?_=1413917541883 (null)

					DiadocSys.Net.Http.Client.HttpClientException: ResponseStatusCode: NONE

					RequestUrl: http://?//v5.3/sessions/CB8509235B37514B948D529C24FF006D521FE0637293354DAA8BB469C6CB8F30

					Could not get response from http cluster ---> System.AggregateException: Can't perform request 'GET /v5.3/sessions/CB8509235B37514B948D529C24FF006D521FE0637293354DAA8BB469C6CB8F30' to cluster authService-v2 ServiceName: authService-v2, EndPoint: https://api.kontur.ru/auth/.

					Body: <null> ---> DiadocSys.Net.Http.Client.ReplicaFailedException: The operation has timed out ---> System.Net.WebException: The operation has timed out

					   at System.Net.HttpWebRequest.GetResponse()

					   at DiadocSys.Net.Http.Client.HttpClient.GetResponse(HttpEndPoint endPoint, IHttpRequest request)

					   --- End of inner exception stack trace ---

					   at DiadocSys.Net.Http.Client.HttpClient.GetResponse(HttpEndPoint endPoint, IHttpRequest request)

					   at DiadocSys.Net.Http.Client.HttpClusterClient.TryGetResponse(IHttpRequest request, HttpReplica replica, ICollection`1 errors)

					   --- End of inner exception stack trace ---

					   --- End of inner exception stack trace ---

					   at DiadocSys.Net.Http.Client.HttpClusterClient.DoGetResponse(IHttpRequest request, Cluster`1 cluster, ICollection`1 errors, Int32 attempt, Int32 maxTryCount)

					   at DiadocSys.Net.Http.Client.HttpClusterClient.DoGetResponse(IHttpRequest request, Cluster`1 cluster, ICollection`1 errors, Int32 attempt, Int32 maxTryCount)

					   at DiadocSys.Net.Http.Client.HttpClusterClient.DoGetResponse(IHttpRequest request, Cluster`1 cluster, ICollection`1 errors, Int32 attempt, Int32 maxTryCount)

					   at DiadocSys.Net.Http.Client.HttpClusterClient.GetResponse(IHttpRequest request, Nullable`1 clientId, Nullable`1 maxTryCount)

					   at DiadocCommons.Portal.Auth.SidAuthServiceClient.PerformRequest(IHttpRequest request, HttpStatusCode[] allowedStatusCodes)

					   at DiadocCommons.Portal.Auth.SidAuthServiceClient.PerformRequest[T](IHttpRequest request, Func`2 getResponse)

					   at DiadocCommons.Portal.Auth.SidAuthServiceClient.GetSessionInfo(IRequestContext requestContext, String sid)

					   at Diadoc.Web.DiadocHttpApplicationBase.Application_AuthenticateRequest(Object sender, EventArgs eventArgs)

					   at System.Web.HttpApplication.SyncEventExecutionStep.System.Web.HttpApplication.IExecutionStep.Execute()

					   at System.Web.HttpApplication.ExecuteStep(IExecutionStep step, Boolean& completedSynchronously)

					""" ,
"""

					Diadoc.Workflow.WorkflowService.DeliveryMachinery.Routing.Document2DepartmentRouter Diadoc.DeliveryManHost Found departments conflicting by address. Department ids: afc977fa-70be-4639-8bb6-ab106fccf074, b4f268b8-ea09-41bf-9ed8-e29525ca40b9 RequestId: 5571fcc1-fdde-4265-8d9f-8af497bb8c78, Thumbprint: df5ab10c7dd77bc14bc224923292ca56a103a6cd, ClientSystemId: diadoc.web, Locale: ru, SessionId: 00000000-0000-0000-0000-000000000000

					0f99d2b1-7354-4ba0-9138-334edab5ef72

					df5ab10c7dd77bc14bc224923292ca56a103a6cd

					635495053255825139

					0

					B1D2990F5473A04B9138334EDAB5EF728E206F51EE29124FBC49F0D136855A5C, UserId: 0f99d2b1-7354-4ba0-9138-334edab5ef72

					""" ,
"""

					DC.Google.Api.Handlers.GetOrganizationInfoHandlerBase DC.Google.Api Timeout at GenerateOrganizationInfoResponse, inn: 7704582421 (null)

					""" ,
"""

					DiaDoc.WebApp.Controllers.Preferences.PreferencesController diadoc.web User has provided wrong combination of e-mail and key: Vyln.Byraavxbi@fhavagreoerj.eh and 63P87955S21N2NR1Q50939S1SS1S470895QR5NS08342OQQS55696PO8SQ04R0Q3P0NN28S0ON (null)

					""" ,
"""

					Diadoc.TimeStampServer.Impl.CrlManagement.CrlDownloader Diadoc.TimeStampServerHost Failed to get crl from: http://KordonCa/certenroll/!0423!0426%20!041e!041e!041e%20!041a!043e!0440!0434!043e!043d.crl (null)

					DiadocSys.Net.Http.Client.ReplicaFailedException: The remote name could not be resolved: 'kordonca' ---> System.Net.WebException: The remote name could not be resolved: 'kordonca'

					   at System.Net.HttpWebRequest.GetResponse()

					   at DiadocSys.Net.Http.Client.HttpClient.GetResponse(HttpEndPoint endPoint, IHttpRequest request) in c:\cement\diadocsys\_Src\DiadocSys.Net.Http\Client\HttpClient.cs:line 35

					   --- End of inner exception stack trace ---

					   at DiadocSys.Net.Http.Client.HttpClient.GetResponse(HttpEndPoint endPoint, IHttpRequest request) in c:\cement\diadocsys\_Src\DiadocSys.Net.Http\Client\HttpClient.cs:line 49

					   at Diadoc.TimeStampServer.Impl.CrlManagement.CrlDownloader.TryGetCrl(IRequestContext context, String cdpUrl) in c:\cement\diadoc\_Src\App\Diadoc.TimeStampServer.Impl\CrlManagement\CrlDownloader.cs:line 45

					""" ,
"""

					Diadoc.FilterIndex.Impl.Update.Document.DocumentIndexUpdaterBase Diadoc.FilterByDocumentDateIndexHost Skipping non-assemblable meta : SpiceForLetter: bc60477f-bff1-4169-ace1-df98bb50f171, Id: 7e30fca1-70eb-4069-bc1b-73af2d05501d, Timestamp: Ticks: 635495389898354257, DateTime: 2014-10-22 01:43:09Z, Box: ca7fe457-542f-4679-87df-60bb9997208f

					SpiceFor:bc60477f-bff1-4169-ace1-df98bb50f171

					From:530f15da-5b60-47f2-b2b8-21b683eb3d37

					To:ca7fe457-542f-4679-87df-60bb9997208f

					CreatedBySystem:diadoc.api:1SBox_3_5-568ef3cd-130e-4194-a473-5c6e4818412d

					 (null)

					""" ,
"""

					DiaDoc.WebApp.Views.Shared.EmployeeRequests.EmployeeRequestController diadoc.web Admin employee not found for organization 221b37e7-c4f9-498a-b887-ef6d46ff8768 (null)

					""" ,
"""

					Diadoc.FnsRegMessagesWatcher.Impl.FnsRegMessagesWatcher Diadoc.FnsRegMessagesWatcherHost FnsRegMessage for participant 2BM-2222031123-2013022103334317777050000000000 with docflowId FB12BCE8B96F1F428673562AC751F5FB failed (null)

					""" ,
"""

					Diadoc.Protocols.BdbIndex.Storage.StorageEnvironment Diadoc.LiveIndexHost reallocated from [100] to [951], values, database (file name [C:\Diadoc\localdata\liveIndex-v2.stale-2014-10-21-08-59-25.db], database name [metas]) (null)

					""" ,
"""

					DiadocCommons.Rabbit.DiadocRabbitClusterClient Diadoc.FnsClaimHost Error while connecting to rabbitmq replica ServiceName: rabbit, EndPoint: 192.168.52.13:5672 (null)

					None of the specified endpoints were reachable

					Endpoints attempted:

					------------------------------------------------

					endpoint=amqp-0-9://192.168.52.13:5672, attempts=1

					RabbitMQ.Client.Exceptions.AlreadyClosedException: Already closed: The AMQP operation was interrupted: AMQP close-reason, initiated by Library, code=541, text="Unexpected Exception", classId=0, methodId=0, cause=System.IO.IOException: Unable to read data from the transport connection: An existing connection was forcibly closed by the remote host. ---> System.Net.Sockets.SocketException: An existing connection was forcibly closed by the remote host

					   at System.Net.Sockets.NetworkStream.Read(Byte[] buffer, Int32 offset, Int32 size)

					   --- End of inner exception stack trace ---

					   at RabbitMQ.Client.Impl.Frame.ReadFrom(NetworkBinaryReader reader)

					   at RabbitMQ.Client.Impl.SocketFrameHandler_0_9.ReadFrame()

					   at RabbitMQ.Client.Impl.ConnectionBase.MainLoopIteration()

					   at RabbitMQ.Client.Impl.ConnectionBase.MainLoop()

					   at RabbitMQ.Client.Impl.SessionBase.Transmit(Command cmd)

					   at RabbitMQ.Client.Impl.MainSession.Transmit(Command cmd)

					   at RabbitMQ.Client.Impl.ConnectionBase.StartAndTune()

					   at RabbitMQ.Client.Framing.Impl.v0_9_1.Connection.Open(Boolean insist)

					   at RabbitMQ.Client.Impl.ConnectionBase..ctor(ConnectionFactory factory, Boolean insist, IFrameHandler frameHandler)

					   at RabbitMQ.Client.Framing.Impl.v0_9_1.ProtocolBase.CreateConnection(ConnectionFactory factory, Boolean insist, IFrameHandler frameHandler)

					   at RabbitMQ.Client.ConnectionFactory.FollowRedirectChain(Int32 maxRedirects, IDictionary`2 connectionAttempts, IDictionary`2 connectionErrors, AmqpTcpEndpoint[]& mostRecentKnownHosts, AmqpTcpEndpoint endpoint)

					================================================

					Stack trace:

					   at RabbitMQ.Client.ConnectionFactory.CreateConnection(Int32 maxRedirects)

					   at DiadocSys.Net.Rabbit.RabbitConnection.TryConnect(Replica replica, UInt16 heartbeat, ICollection`1 errors) in c:\cement\diadocsys\_Src\DiadocSys.Net.Rabbit\RabbitConnection.cs:line 126

					""" ,
"""

					Diadoc.FnsClaim.ClientImpl.Storage.Database.CompositeClaimStorage diadoc.web Secondary storage fault: Cannot perform request to replica: ServiceName: claim-v2, ConnectionString: Server=dd15;Database=diadoc;Uid=claim;Pwd="Bcnht,jdfybzCenmDtotq";Unicode=True;Validate Connection=True;Default Command Timeout=30;Connection Timeout=5, ReplicaType: Master, Error: ErrorCode: , ErrorMessage: Connection must be opened. (null)

					""" ,
"""

					Diadoc.UserService.Impl.UserEmployeesMigrator Diadoc.KeNotificationIndexHost Migration caused employee conflict: from EmployeeId: f801f022-4eb9-452b-9a34-5b31f2c2fd01, OrgId: d7e399d9-5b7e-4bb2-a695-996e346cd796, UserId: 67ad8ad0-f73e-4fd6-a77c-378165bdde29, Position: , IsAdmin: True, CanSignDocuments: True, CanAddResolutions: True, CanRequestResolutions: True, DocumentAccessLevel: DepartmentAndSubdepartments, DepartmentId: , SelectedDepartmentIds:  to EmployeeId: 712b3716-3009-48a1-b3b9-f431846b1a51, OrgId: d7e399d9-5b7e-4bb2-a695-996e346cd796, UserId: c3c4f4cc-7529-4da3-9e0c-a0b47debdd30, Position: , IsAdmin: True, CanSignDocuments: True, CanAddResolutions: True, CanRequestResolutions: True, DocumentAccessLevel: DepartmentAndSubdepartments, DepartmentId: , SelectedDepartmentIds:  (null)

					""" ,
"""

					Diadoc.FnsClaim.ClientImpl.Storage.Database.ClaimedDocumentDatabaseCluster diadoc.web Cannot perform request to replica: ServiceName: claim-v2, ConnectionString: Server=dd15;Database=diadoc;Uid=claim;Pwd="Bcnht,jdfybzCenmDtotq";Unicode=True;Validate Connection=True;Default Command Timeout=30;Connection Timeout=5, ReplicaType: Master, Error: Claim with Id aed3a31d-8b0a-49e1-8086-2654d5e69be1 can not be found (null)

					Diadoc.FnsClaim.Storage.ClaimNotFoundException: Claim with Id aed3a31d-8b0a-49e1-8086-2654d5e69be1 can not be found

					   at Diadoc.FnsClaim.ClientImpl.Storage.Database.MysqlClaimStorage.FindClaimProperties(Guid claimId, IDatabaseTransaction transactDb, Boolean createNew)

					   at Diadoc.FnsClaim.ClientImpl.Storage.Database.MysqlClaimStorage.<>c__DisplayClass2c.<GetClaimProperties>b__2b(IDatabaseTransaction transactDb)

					   at Diadoc.FnsClaim.ClientImpl.Storage.Database.MysqlClaimDatabase.<>c__DisplayClass2`1.<PerformSelectRequest>b__1(IDatabase db)

					   at DiadocSys.Net.MySql.MySql.MySqlClusterClient.<>c__DisplayClass6`1.<PerformReadonlyRequest>b__5(DbManager db)

					   at DiadocSys.Net.MySql.MySql.MySqlClusterClient.<>c__DisplayClassb`1.<DoPerformRequest>b__a(DbManager db)

					   at DiadocSys.Net.MySql.MySql.MySqlClusterClient.TryPerformRequest(IRequestContext requestContext, Action`1 requestAction, MySqlReplica replica, ICollection`1 errors, Boolean allowRetry)

					""" ,
"""

					Diadoc.Web.Commons.HttpApplicationBase diadoc.web Unhandled exception. RequestId: 27aacd5f-7908-4401-8d62-e3e40a981ad5, ClientSystemId: diadoc.web, Locale: ru, SessionId: 00000000-0000-0000-0000-000000000000

					e531dc67-1d67-43e6-8df0-d67913cf0ea6



					635495108660256041

					0

					, UserId: e531dc67-1d67-43e6-8df0-d67913cf0ea6, Url: http://diadoc.kontur.ru/6f5d55d1-9491-4301-8245-32112b7f278d/ReceiptSign/ReceiptsForSignature?_=1413914090569 (null)

					System.InvalidOperationException: Неправильное имя физического лица '  '

					   at DiadocFormats.Gnivc.Patchers.XmlSignerCreator.CreateReceiptSigner(XmlPatchingContext context)

					   at DiaDoc.WebApp.Views.Shared.ReceiptAutosigner.ReceiptSignController.ReceiptsForSignature(String batchKey, IEmployeeRequestContext requestContext, DiadocUserInfo userInfo)

					   at lambda_method(Closure , ControllerBase , Object[] )

					   at System.Web.Mvc.ReflectedActionDescriptor.Execute(ControllerContext controllerContext, IDictionary`2 parameters)

					   at System.Web.Mvc.ControllerActionInvoker.InvokeActionMethod(ControllerContext controllerContext, ActionDescriptor actionDescriptor, IDictionary`2 parameters)

					   at System.Web.Mvc.ControllerActionInvoker.<>c__DisplayClass15.<InvokeActionMethodWithFilters>b__12()

					   at System.Web.Mvc.ControllerActionInvoker.InvokeActionMethodFilter(IActionFilter filter, ActionExecutingContext preContext, Func`1 continuation)

					   at System.Web.Mvc.ControllerActionInvoker.InvokeActionMethodFilter(IActionFilter filter, ActionExecutingContext preContext, Func`1 continuation)

					   at System.Web.Mvc.ControllerActionInvoker.InvokeActionMethodWithFilters(ControllerContext controllerContext, IList`1 filters, ActionDescriptor actionDescriptor, IDictionary`2 parameters)

					   at System.Web.Mvc.ControllerActionInvoker.InvokeAction(ControllerContext controllerContext, String actionName)

					   at System.Web.Mvc.Controller.ExecuteCore()

					   at System.Web.Mvc.ControllerBase.Execute(RequestContext requestContext)

					   at System.Web.Mvc.MvcHandler.<>c__DisplayClass6.<>c__DisplayClassb.<BeginProcessRequest>b__5()

					   at System.Web.Mvc.Async.AsyncResultWrapper.<>c__DisplayClass1.<MakeVoidDelegate>b__0()

					   at System.Web.Mvc.MvcHandler.<>c__DisplayClasse.<EndProcessRequest>b__d()

					   at System.Web.HttpApplication.CallHandlerExecutionStep.System.Web.HttpApplication.IExecutionStep.Execute()

					   at System.Web.HttpApplication.ExecuteStep(IExecutionStep step, Boolean& completedSynchronously)

					""" ,
"""

					DiadocCommons.Rabbit.DiadocRabbitClusterClient Diadoc.FnsClaimHost Can not dispose connection (null)

					RabbitMQ.Client.Exceptions.OperationInterruptedException: The AMQP operation was interrupted

					   at RabbitMQ.Client.Impl.ConnectionBase.System.IDisposable.Dispose()

					   at DiadocSys.Net.Rabbit.RabbitConnection.Disconnect() in c:\cement\diadocsys\_Src\DiadocSys.Net.Rabbit\RabbitConnection.cs:line 102

					""" ,
"""

					Diadoc.Kanso Diadoc.DeliveryManHost [KansoWrite-185202680645] AsyncWebRequestClient. Failed to send request body to 192.168.58.13:8877.

						Exception: System.NotSupportedException: The stream does not support concurrent IO read or write operations.

					   at System.Net.ConnectStream.InternalWrite(Boolean async, Byte[] buffer, Int32 offset, Int32 size, AsyncCallback callback, Object state)

					   at System.Net.ConnectStream.BeginWrite(Byte[] buffer, Int32 offset, Int32 size, AsyncCallback callback, Object state)

					   at Kontur.Http.Common.ByteArrayContent.BeginWriteToStream(Stream stream, Action onSuccess, Action`1 onError) in f:\Projects\cement-projects\kanso\Http\Common\ByteArrayContent.cs:line 41 (null)

					""" ,
"""

					Diadoc.Handlers.FnsReg.Impl.FnsRegMessageHandler Diadoc.FnsRegHost Duplicate task detected: {"FakeDocflowId":"c75785fc-e918-4771-ae17-d1edd9be6ae2","FnsParticipantId":"2BM-6501114659-2012052808321961022630000000000","FnsRegistrationDate":"25.10.2013","Organization":{"Name":"ОБЩЕСТВО С ОГРАНИЧЕННОЙ ОТВЕТСТВЕННОСТЬЮ \"САХАЛИН МАШИНЕРИ\"","Inn":"6501114659","Kpp":"650101001","Ogrn":"1026500523686","TaxInspCode":"6501","Address":{"ZipCode":"693012","Region":"65","Territory":null,"City":"Южно-Сахалинск","Locality":null,"Street":"пр-кт Мира","Building":"1Б/1","Block":null,"Apartment":null}},"Certificates":[{"BeginDate":"06.11.2013","EndDate":"06.11.2014","Certificate":"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"},{"BeginDate":"06.11.2013","EndDate":"06.11.2014","Certificate":"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"},{"BeginDate":"29.10.2013","EndDate":"29.10.2014","Certificate":"MIIKYjCCChGgAwIBAgIKclOxPwAAAAKGjzAIBgYqhQMCAgMwggF4MRgwFgYFKoUDZAESDTEwMjY2MDU2MDY2MjAxGjAYBggqhQMDgQMBARIMMDA2NjYzMDAzMTI3MTcwNQYDVQQJDC7Qn9GA0L7RgdC/0LXQutGCINCa0L7RgdC80L7QvdCw0LLRgtC+0LIg0LQuIDU2MR4wHAYJKoZIhvcNAQkBFg9jYUBza2Jrb250dXIucnUxCzAJBgNVBAYTAlJVMTMwMQYDVQQIDCo2NiDQodCy0LXRgNC00LvQvtCy0YHQutCw0Y8g0L7QsdC70LDRgdGC0YwxITAfBgNVBAcMGNCV0LrQsNGC0LXRgNC40L3QsdGD0YDQszErMCkGA1UECgwi0JfQkNCeICLQn9CkICLQodCa0JEg0JrQvtC90YLRg9GAIjEwMC4GA1UECwwn0KPQtNC+0YHRgtC+0LLQtdGA0Y/RjtGJ0LjQuSDRhtC10L3RgtGAMSMwIQYDVQQDExpTS0IgS29udHVyIHBy

					""" ,
"""

					Diadoc.FnsClaim.ClientImpl.Storage.Database.CompositeClaimStorage diadoc.web Secondary storage failed with error Document ab79d844-7bd5-4987-a256-352f4159e4fb of claim 0db4e6fa-729c-4533-b588-cb3deb17c198 does not exist while primary storage failed with error Cannot perform request to replica: ServiceName: claim-v2, ConnectionString: Server=dd15;Database=diadoc;Uid=claim;Pwd="Bcnht,jdfybzCenmDtotq";Unicode=True;Validate Connection=True;Default Command Timeout=30;Connection Timeout=5, ReplicaType: Master, Error: Document with id = ab79d844-7bd5-4987-a256-352f4159e4fb doesn't exist (null)

					""" ,
"""

					Diadoc.Commons.MySql.ReferencesDatabaseCluster diadoc.web Cannot perform request to replica: ServiceName: references-v2, ConnectionString: Server=dd08;Database=diadoc;Uid=diadoc;Pwd=Rxabk26w27QrqYlc;Unicode=True;Validate Connection=True;Default Command Timeout=30;Connection Timeout=5, ReplicaType: Master, Error: ErrorCode: 2013, ErrorMessage: Lost connection to MySQL server during query (null)

					BLToolkit.Data.DataException: Lost connection to MySQL server during query ---> Devart.Data.MySql.MySqlException: Lost connection to MySQL server during query ---> System.TimeoutException: Server did not respond within the specified timeout interval. ---> System.IO.IOException: Unable to read data from the transport connection: A connection attempt failed because the connected party did not properly respond after a period of time, or established connection failed because connected host has failed to respond. ---> System.Net.Sockets.SocketException: A connection attempt failed because the connected party did not properly respond after a period of time, or established connection failed because connected host has failed to respond

					   at System.Net.Sockets.NetworkStream.Read(Byte[] buffer, Int32 offset, Int32 size)

					   --- End of inner exception stack trace ---

					   at System.Net.Sockets.NetworkStream.Read(Byte[] buffer, Int32 offset, Int32 size)

					   at Devart.Common.ad.a(Byte[] A_0, Int32 A_1, Int32 A_2)

					   --- End of inner exception stack trace ---

					   at Devart.Common.ad.a(Byte[] A_0, Int32 A_1, Int32 A_2)

					   at Devart.Common.w.c(Byte[] A_0, Int32 A_1, Int32 A_2)

					   at Devart.Common.ae.d(Byte[] A_0, Int32 A_1, Int32 A_2)

					   --- End of inner exception stack trace ---

					   at Devart.Data.MySql.aw.d(Exception A_0)

					   at Devart.Common.ae.d(Byte[] A_0, Int32 A_1, Int32 A_2)

					   at Devart.Data.MySql.c.n()

					   at Devart.Data.MySql.c.h()

					   at Devart.Data.MySql.u.a(a4[]& A_0, Int32& A_1)

					   at Devart.Data.MySql.u.a(Byte[] A_0, Int32 A_1, Boolean A_2)

					   at Devart.Data.MySql.k.e()

					   at Devart.Data.MySql.MySqlCommand.InternalExecute(CommandBehavior behavior, IDisposable stmt, Int32 startRecord, Int32 maxRecords)

					   at Devart.Common.DbCommandBase.ExecuteDbDataReader(CommandBehavior behavior, Boolean nonQuery)

					   at Devart.Common.DbCommandBase.ExecuteNonQuery()

					   at BLToolkit.Data.DbManager.ExecuteOperation[T](OperationType operationType, Func`1 operation)

					   --- End of inner exception stack trace ---

					   at BLToolkit.Data.DbManager.OnOperationException(OperationType op, DataException ex)

					   at BLToolkit.Data.DbManager.HandleOperationException(OperationType op, Exception ex)

					   at BLToolkit.Data.DbManager.ExecuteOperation[T](OperationType operationType, Func`1 operation)

					   at BLToolkit.Data.DbManager.ExecuteNonQueryInternal()

					   at BLToolkit.Data.DbManager.ExecuteNonQuery()

					   at BLToolkit.Data.DbManager.BLToolkit.Data.Linq.IDataContext.ExecuteNonQuery(Object query)

					   at BLToolkit.Data.Linq.Query`1.NonQueryQuery(IDataContextInfo dataContextInfo, Expression expr, Object[] parameters)

					   at BLToolkit.Data.Linq.Query`1.<SetNonQueryQuery>b__e(QueryContext ctx, IDataContextInfo db, Expression expr, Object[] ps)

					   at BLToolkit.Data.Linq.ExpressionQuery`1.System.Linq.IQueryProvider.Execute[TResult](Expression expression)

					   at BLToolkit.Data.Linq.LinqExtensions.InsertOrUpdate[T](Table`1 target, Expression`1 insertSetter, Expression`1 onDuplicateKeyUpdateSetter)

					   at DiadocSys.Net.MySql.MySql.MySqlClusterClient.<>c__DisplayClassb`1.<DoPerformRequest>b__a(DbManager db)

					   at DiadocSys.Net.MySql.MySql.MySqlClusterClient.TryPerformRequest(IRequestContext requestContext, Action`1 requestAction, MySqlReplica replica, ICollection`1 errors, Boolean allowRetry)

					""" ,
"""

					Diadoc.Workflow.DocumentService.Patching.InvoicePatching.InvoicePatcher diadoc.web Failed to patch invoice (null)

					System.InvalidOperationException: Неправильное имя физического лица '  '

					   at DiadocFormats.Gnivc.Patchers.XmlSignerCreator.CreateJuridicalSigner(XmlPatchingContext context)

					   at Diadoc.Workflow.DocumentService.Patching.InvoicePatching.InvoicePatcher.Patch(ФайлДокументПодписант currentValue, XmlPatchingContext context)

					   at Diadoc.Workflow.DocumentService.Patching.InvoicePatching.InvoicePatcher.PatchInvoiceDocument(XmlPatchingContext context, ФайлДокумент документ)

					   at Diadoc.Workflow.DocumentService.Patching.InvoicePatching.InvoicePatcher.PatchInvoice(Byte[] invoiceBytes, XmlPatchingContext context)

					""" ,
"""

					Diadoc.FnsClaim.ClientImpl.Storage.Database.CompositeClaimStorage diadoc.web Secondary storage fault: Document 9ca5d35a-6927-48a3-8bb1-e186e52fb86b of claim 4fd17e88-ad93-4080-8d63-43fd65d8dc6b does not exist (null)

					""" ,
"""

					Diadoc.Web.Commons.HttpApplicationBase diadoc.web Unhandled exception. RequestId: b655ac02-2cdd-4688-b26c-dae27db9ed0a, Thumbprint: 552bbbd81fb161cf3efa79fd6a71ff30315bd792, ClientSystemId: diadoc.web, Locale: ru, SessionId: 00000000-0000-0000-0000-000000000000

					adee3a08-bee2-4f3e-8e0d-554d48336f45

					552bbbd81fb161cf3efa79fd6a71ff30315bd792

					635495148045356803

					0

					083AEEADE2BE3E4F8E0D554D48336F45DBBE605D0E2F3349AA3FE43E502A1BDC, UserId: adee3a08-bee2-4f3e-8e0d-554d48336f45, Url: http://diadoc.kontur.ru/f40c02ae-5e68-4927-ba55-a90699562526/FirstEnter/NotifyWizardShown (null)

					System.InvalidOperationException: Could not perform request to mysql cluster. ---> System.AggregateException: One or more errors occurred. ---> BLToolkit.Data.DataException: Lost connection to MySQL server during query ---> Devart.Data.MySql.MySqlException: Lost connection to MySQL server during query ---> System.TimeoutException: Server did not respond within the specified timeout interval. ---> System.IO.IOException: Unable to read data from the transport connection: A connection attempt failed because the connected party did not properly respond after a period of time, or established connection failed because connected host has failed to respond. ---> System.Net.Sockets.SocketException: A connection attempt failed because the connected party did not properly respond after a period of time, or established connection failed because connected host has failed to respond

					   at System.Net.Sockets.NetworkStream.Read(Byte[] buffer, Int32 offset, Int32 size)

					   --- End of inner exception stack trace ---

					   at System.Net.Sockets.NetworkStream.Read(Byte[] buffer, Int32 offset, Int32 size)

					   at Devart.Common.ad.a(Byte[] A_0, Int32 A_1, Int32 A_2)

					   --- End of inner exception stack trace ---

					   at Devart.Common.ad.a(Byte[] A_0, Int32 A_1, Int32 A_2)

					   at Devart.Common.w.c(Byte[] A_0, Int32 A_1, Int32 A_2)

					   at Devart.Common.ae.d(Byte[] A_0, Int32 A_1, Int32 A_2)

					   --- End of inner exception stack trace ---

					   at Devart.Data.MySql.aw.d(Exception A_0)

					   at Devart.Common.ae.d(Byte[] A_0, Int32 A_1, Int32 A_2)

					   at Devart.Data.MySql.c.n()

					   at Devart.Data.MySql.c.h()

					   at Devart.Data.MySql.u.a(a4[]& A_0, Int32& A_1)

					   at Devart.Data.MySql.u.a(Byte[] A_0, Int32 A_1, Boolean A_2)

					   at Devart.Data.MySql.k.e()

					   at Devart.Data.MySql.MySqlCommand.InternalExecute(CommandBehavior behavior, IDisposable stmt, Int32 startRecord, Int32 maxRecords)

					   at Devart.Common.DbCommandBase.ExecuteDbDataReader(CommandBehavior behavior, Boolean nonQuery)

					   at Devart.Common.DbCommandBase.ExecuteNonQuery()

					   at BLToolkit.Data.DbManager.ExecuteOperation[T](OperationType operationType, Func`1 operation)

					   --- End of inner exception stack trace ---

					   at BLToolkit.Data.DbManager.OnOperationException(OperationType op, DataException ex)

					   at BLToolkit.Data.DbManager.HandleOperationException(OperationType op, Exception ex)

					   at BLToolkit.Data.DbManager.ExecuteOperation[T](OperationType operationType, Func`1 operation)

					   at BLToolkit.Data.DbManager.ExecuteNonQueryInternal()

					   at BLToolkit.Data.DbManager.ExecuteNonQuery()

					   at BLToolkit.Data.DbManager.BLToolkit.Data.Linq.IDataContext.ExecuteNonQuery(Object query)

					   at BLToolkit.Data.Linq.Query`1.NonQueryQuery(IDataContextInfo dataContextInfo, Expression expr, Object[] parameters)

					   at BLToolkit.Data.Linq.Query`1.<SetNonQueryQuery>b__e(QueryContext ctx, IDataContextInfo db, Expression expr, Object[] ps)

					   at BLToolkit.Data.Linq.ExpressionQuery`1.System.Linq.IQueryProvider.Execute[TResult](Expression expression)

					   at BLToolkit.Data.Linq.LinqExtensions.InsertOrUpdate[T](Table`1 target, Expression`1 insertSetter, Expression`1 onDuplicateKeyUpdateSetter)

					   at DiadocSys.Net.MySql.MySql.MySqlClusterClient.<>c__DisplayClassb`1.<DoPerformRequest>b__a(DbManager db)

					   at DiadocSys.Net.MySql.MySql.MySqlClusterClient.TryPerformRequest(IRequestContext requestContext, Action`1 requestAction, MySqlReplica replica, ICollection`1 errors, Boolean allowRetry)

					   --- End of inner exception stack trace ---

					   --- End of inner exception stack trace ---

					   at DiadocSys.Net.MySql.MySql.MySqlClusterClient.DoPerformRequest(IRequestContext requestContext, Action`1 requestAction, Cluster`1 cluster, ICollection`1 errors, Int32 attempt, Boolean allowRetry)

					   at DiadocSys.Net.MySql.MySql.MySqlClusterClient.DoPerformRequest(IRequestContext requestContext, Action`1 requestAction, Cluster`1 cluster, ICollection`1 errors, Int32 attempt, Boolean allowRetry)

					   at DiadocSys.Net.MySql.MySql.MySqlClusterClient.DoPerformRequest(IRequestContext requestContext, Action`1 requestAction, Cluster`1 cluster, ICollection`1 errors, Int32 attempt, Boolean allowRetry)

					   at DiadocSys.Net.MySql.MySql.MySqlClusterClient.DoPerformRequest[T](IRequestContext requestContext, Func`2 requestAction, Cluster`1 cluster, Boolean allowRetry)

					   at DiadocSys.Net.MySql.DatabaseCluster.PerformRetryableWriteRequest[T](IDatabaseRequestContext context, Func`2 requestAction)

					   at Diadoc.Protocols.Database.VisualInfo.VisualInfoDb.UpdateForOrgAndUser(IRequestContext requestContext, Guid orgId, Guid userId, String type, String data)

					   at Diadoc.Protocols.Database.VisualInfo.VisualInfoDb.UpdateForUser(IRequestContext requestContext, Guid userId, String type, String data)

					   at Diadoc.Model.FirstEnterLightboxes.FirstEnterVisualInfoService.UpdateForUser(IEmployeeRequestContext requestContext, String dialogType)

					   at Diadoc.Model.FirstEnterLightboxes.FirstEnterVisualInfoService.RemoveMustBeShownVisualInfos(IEmployeeRequestContext requestContext, List`1 visualInfos)

					   at System.Web.Mvc.ActionMethodDispatcher.<>c__DisplayClass1.<WrapVoidAction>b__0(ControllerBase controller, Object[] parameters)

					   at System.Web.Mvc.ReflectedActionDescriptor.Execute(ControllerContext controllerContext, IDictionary`2 parameters)

					   at System.Web.Mvc.ControllerActionInvoker.InvokeActionMethod(ControllerContext controllerContext, ActionDescriptor actionDescriptor, IDictionary`2 parameters)

					   at System.Web.Mvc.ControllerActionInvoker.<>c__DisplayClass15.<InvokeActionMethodWithFilters>b__12()

					   at System.Web.Mvc.ControllerActionInvoker.InvokeActionMethodFilter(IActionFilter filter, ActionExecutingContext preContext, Func`1 continuation)

					   at System.Web.Mvc.ControllerActionInvoker.InvokeActionMethodFilter(IActionFilter filter, ActionExecutingContext preContext, Func`1 continuation)

					   at System.Web.Mvc.ControllerActionInvoker.InvokeActionMethodWithFilters(ControllerContext controllerContext, IList`1 filters, ActionDescriptor actionDescriptor, IDictionary`2 parameters)

					   at System.Web.Mvc.ControllerActionInvoker.InvokeAction(ControllerContext controllerContext, String actionName)

					   at System.Web.Mvc.Controller.ExecuteCore()

					   at System.Web.Mvc.ControllerBase.Execute(RequestContext requestContext)

					   at System.Web.Mvc.MvcHandler.<>c__DisplayClass6.<>c__DisplayClassb.<BeginProcessRequest>b__5()

					   at System.Web.Mvc.Async.AsyncResultWrapper.<>c__DisplayClass1.<MakeVoidDelegate>b__0()

					   at System.Web.HttpApplication.CallHandlerExecutionStep.System.Web.HttpApplication.IExecutionStep.Execute()

					   at System.Web.HttpApplication.ExecuteStep(IExecutionStep step, Boolean& completedSynchronously)

					""" ,
"""

					WebAdminApp.Helpers.EmployeeAndBoxAclUpdater diadoc.webadmin Create user 681e71c7-b201-412f-a520-abb67b61265d (null)

					""" ,
"""

					Diadoc.Protocols.Portal.PortalAuth.AuthTokenAccessor`1[[Diadoc.App.Common.DiadocToken, Diadoc.App.Common, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]] Diadoc.OvermindHost Failed to extract token from: Invali (null)

					System.FormatException: Invalid length for a Base-64 char array or string.

					   at System.Convert.FromBase64_Decode(Char* startInputPtr, Int32 inputLength, Byte* startDestPtr, Int32 destLength)

					   at System.Convert.FromBase64CharPtr(Char* inputPtr, Int32 inputLength)

					   at System.Convert.FromBase64String(String s)

					   at Diadoc.Protocols.Portal.PortalAuth.AuthTokenAccessor`1.TryExtractToken(String base64EncodedToken) in c:\cement\diadoc\_Src\Common\Diadoc.Protocols.Portal\PortalAuth\AuthTokenAccessor.cs:line 27

					""" ,
"""

					DiadocCommons.Rabbit.DiadocRabbitClusterClient Diadoc.FnsClaimHost Can not dequeue (null)

					RabbitMQ.Client.Exceptions.AlreadyClosedException: Already closed: The AMQP operation was interrupted: AMQP close-reason, initiated by Library, code=0, text="End of stream", classId=0, methodId=0, cause=System.IO.EndOfStreamException: Heartbeat missing with heartbeat == 5 seconds

					   at RabbitMQ.Client.Impl.SessionBase.Transmit(Command cmd)

					   at DiadocSys.Net.Rabbit.RabbitQueue`1.AckEvent(Subscription subscription, BasicDeliverEventArgs basicDeliveryEventArgs) in c:\cement\diadocsys\_Src\DiadocSys.Net.Rabbit\RabbitQueue.cs:line 99

					   at DiadocSys.Net.Rabbit.RabbitQueue`1.TryDequeue(Action`1 processEvent, Nullable`1 timeout) in c:\cement\diadocsys\_Src\DiadocSys.Net.Rabbit\RabbitQueue.cs:line 55

					""" ,
"""

					DiaDoc.WebApp.Controllers.Send.NonformalizedAttachmentModelProvider diadoc.web Document recognition error: System.NotSupportedException: Cannot recognize document (invalid format) ---> System.ArgumentException: The supplied POIFSFileSystem does not contain a BIFF8 'Workbook' entry. Is it really an excel file?

					   at NPOI.HSSF.UserModel.HSSFWorkbook.GetWorkbookDirEntryName(DirectoryNode directory)

					   at NPOI.HSSF.UserModel.HSSFWorkbook..ctor(DirectoryNode directory, Boolean preserveNodes)

					   at NPOI.HSSF.UserModel.HSSFWorkbook..ctor(DirectoryNode directory, POIFSFileSystem fs, Boolean preserveNodes)

					   at NPOI.HSSF.UserModel.HSSFWorkbook..ctor(POIFSFileSystem fs, Boolean preserveNodes)

					   at NPOI.HSSF.UserModel.HSSFWorkbook..ctor(Stream s, Boolean preserveNodes)

					   at NPOI.HSSF.UserModel.HSSFWorkbook..ctor(Stream s)

					   at FieldsRecognition.DocumentModel.Excel.ExcelModelBuilder..ctor(Stream stream)

					   at FieldsRecognition.DocumentModel.Excel.ExcelModelBuilder.BuilderFrom(Stream stream)

					   --- End of inner exception stack trace ---

					   at FieldsRecognition.DocumentModel.Excel.ExcelModelBuilder.BuilderFrom(Stream stream)

					   at DiaDoc.WebApp.Controllers.Send.NonformalizedAttachmentModelProvider.GetAttachment2Send(Byte[] fileContent, String filename, ClientContentLocation serverSideLocation)

					   at DiaDoc.WebApp.Controllers.Send.NonformalizedAttachmentModelProvider.TryGetAttachment2Send(Byte[] fileContent, String filename, ClientContentLocation serverSideLocation) (null)

					""" ,
"""

					Diadoc.FnsClaim.ClientImpl.Storage.Database.ClaimedDocumentDatabaseCluster diadoc.web Cannot perform request to replica: ServiceName: claim-v2, ConnectionString: Server=dd15;Database=diadoc;Uid=claim;Pwd="Bcnht,jdfybzCenmDtotq";Unicode=True;Validate Connection=True;Default Command Timeout=30;Connection Timeout=5, ReplicaType: Master, Error: Document with id = ab79d844-7bd5-4987-a256-352f4159e4fb doesn't exist (null)

					System.InvalidOperationException: Document with id = ab79d844-7bd5-4987-a256-352f4159e4fb doesn't exist

					   at Diadoc.FnsClaim.ClientImpl.Storage.Database.MysqlClaimStorageV1.MysqlClaim.RemoveDocument(Guid documentId)

					   at Diadoc.FnsClaim.ClientImpl.Storage.Database.MysqlClaimStorageV1.<>c__DisplayClass13.<RemoveDocument>b__12(MysqlClaim claim)

					   at Diadoc.FnsClaim.ClientImpl.Storage.Database.MysqlClaimStorageV1.<>c__DisplayClass22.<WithClaimImpl>b__21(MysqlClaim claim)

					   at Diadoc.FnsClaim.ClientImpl.Storage.Database.MysqlClaimStorageV1.<>c__DisplayClass26`1.<WithClaimImpl>b__24(IDatabase db)

					   at DiadocSys.Net.MySql.MySql.MySqlClusterClient.TryPerformRequest(IRequestContext requestContext, Action`1 requestAction, MySqlReplica replica, ICollection`1 errors, Boolean allowRetry)

					""" ,
"""

					Diadoc.Registration.Auto.QualifiedCertificateOrganizationRegistrator diadoc.web Qualified certificate Thumbprint: 4BFD640F9D2D6AA02540DF6B4987C80AB97ABDDE, Inn: 7724777676, OrgName: ООО "ПСК МОССТРОЙМОНТАЖ" auto-registration skipped - registration of default billing account was failed (null)

					""" ,
"""

					DiadocSys.Storage.Framework.EventHandlerHost`1[[Diadoc.Relations.Impl.Storage.RelationEvent, Diadoc.Relations.Impl, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]] Diadoc.ActivityHost Failed to handle Event Timestamp: Ticks: 635495148770269545, DateTime: 2014-10-21 19:01:17Z, EventType: IAcceptedHisInvitation, MyOrgId: 95b89d8e-d0e3-4a43-8c23-59c8c0eb53f4, CounteragentOrgId: f2eaeaef-d113-4c6b-bd8c-1d024cb1a987, PreviousEventTimestamp: Ticks: 635492313762778929, DateTime: 2014-10-18 12:16:16Z, Message: , RelationDocument: LetterId: 6d44e815-1332-4010-abcf-6bded750c47a, EntityId: ec0e4043-ccde-499b-b736-5c2a8dffb3b5, RequestedSignature: True from offset 1274807584 by handler Diadoc.Organizations.ActivityWatcher.ActivityByCounteragentsUpdater exception

					System.InvalidOperationException: Could not perform request to mysql cluster. ---> System.AggregateException: One or more errors occurred. ---> BLToolkit.Data.DataException: Lost connection to MySQL server during query ---> Devart.Data.MySql.MySqlException: Lost connection to MySQL server during query ---> System.TimeoutException: Server did not respond within the specified timeout interval. ---> System.IO.IOException: Unable to read data from the transport connection: A connection attempt failed because the connected party did not properly respond after a period of time, or established connection failed because connected host has failed to respond. ---> System.Net.Sockets.SocketException: A connection attempt failed because the connected party did not properly respond after a period of time, or established connection failed because connected host has failed to respond

					   at System.Net.Sockets.NetworkStream.Read(Byte[] buffer, Int32 offset, Int32 size)

					   --- End of inner exception stack trace ---

					   at System.Net.Sockets.NetworkStream.Read(Byte[] buffer, Int32 offset, Int32 size)

					   at Devart.Common.ad.a(Byte[] A_0, Int32 A_1, Int32 A_2)

					   --- End of inner exception stack trace ---

					   at Devart.Common.ad.a(Byte[] A_0, Int32 A_1, Int32 A_2)

					   at Devart.Common.w.c(Byte[] A_0, Int32 A_1, Int32 A_2)

					   at Devart.Common.ae.d(Byte[] A_0, Int32 A_1, Int32 A_2)

					   --- End of inner exception stack trace ---

					   at Devart.Data.MySql.aw.d(Exception A_0)

					   at Devart.Common.ae.d(Byte[] A_0, Int32 A_1, Int32 A_2)

					   at Devart.Data.MySql.c.n()

					   at Devart.Data.MySql.c.h()

					   at Devart.Data.MySql.u.a(a4[]& A_0, Int32& A_1)

					   at Devart.Data.MySql.u.a(Byte[] A_0, Int32 A_1, Boolean A_2)

					   at Devart.Data.MySql.k.e()

					   at Devart.Data.MySql.MySqlCommand.InternalExecute(CommandBehavior behavior, IDisposable stmt, Int32 startRecord, Int32 maxRecords)

					   at Devart.Common.DbCommandBase.ExecuteDbDataReader(CommandBehavior behavior, Boolean nonQuery)

					   at Devart.Common.DbCommandBase.ExecuteNonQuery()

					   at BLToolkit.Data.DbManager.ExecuteOperation[T](OperationType operationType, Func`1 operation) in e:\Work\dev\.net\bltoolkit\Source\Data\DbManager.cs:line 4437

					   --- End of inner exception stack trace ---

					   at BLToolkit.Data.DbManager.OnOperationException(OperationType op, DataException ex) in e:\Work\dev\.net\bltoolkit\Source\Data\DbManager.cs:line 611

					   at BLToolkit.Data.DbManager.HandleOperationException(OperationType op, Exception ex) in e:\Work\dev\.net\bltoolkit\Source\Data\DbManager.cs:line 4459

					   at BLToolkit.Data.DbManager.ExecuteOperation[T](OperationType operationType, Func`1 operation) in e:\Work\dev\.net\bltoolkit\Source\Data\DbManager.cs:line 4445

					   at BLToolkit.Data.DbManager.ExecuteNonQueryInternal() in e:\Work\dev\.net\bltoolkit\Source\Data\DbManager.cs:line 633

					   at BLToolkit.Data.DbManager.ExecuteNonQuery() in e:\Work\dev\.net\bltoolkit\Source\Data\DbManager.cs:line 2819

					   at BLToolkit.Data.DbManager.BLToolkit.Data.Linq.IDataContext.ExecuteNonQuery(Object query) in e:\Work\dev\.net\bltoolkit\Source\Data\DbManager.Linq.cs:line 191

					   at BLToolkit.Data.Linq.Query`1.NonQueryQuery(IDataContextInfo dataContextInfo, Expression expr, Object[] parameters) in e:\Work\dev\.net\bltoolkit\Source\Data\Linq\Query.cs:line 246

					   at BLToolkit.Data.Linq.Query`1.<SetNonQueryQuery>b__e(QueryContext ctx, IDataContextInfo db, Expression expr, Object[] ps) in e:\Work\dev\.net\bltoolkit\Source\Data\Linq\Query.cs:line 234

					   at BLToolkit.Data.Linq.ExpressionQuery`1.System.Linq.IQueryProvider.Execute[TResult](Expression expression) in e:\Work\dev\.net\bltoolkit\Source\Data\Linq\ExpressionQuery.cs:line 135

					   at BLToolkit.Data.Linq.LinqExtensions.InsertOrUpdate[T](Table`1 target, Expression`1 insertSetter, Expression`1 onDuplicateKeyUpdateSetter) in e:\Work\dev\.net\bltoolkit\Source\Data\Linq\LinqExtensions.cs:line 612

					   at DiadocSys.Net.MySql.MySql.MySqlClusterClient.<>c__DisplayClassb`1.<DoPerformRequest>b__a(DbManager db) in c:\cement\diadocsys\_Src\DiadocSys.Net.MySql\MySql\MySqlClusterClient.cs:line 108

					   at DiadocSys.Net.MySql.MySql.MySqlClusterClient.TryPerformRequest(IRequestContext requestContext, Action`1 requestAction, MySqlReplica replica, ICollection`1 errors, Boolean allowRetry) in c:\cement\diadocsys\_Src\DiadocSys.Net.MySql\MySql\MySqlClusterClient.cs:line 144

					   --- End of inner exception stack trace ---

					   --- End of inner exception stack trace ---

					   at DiadocSys.Net.MySql.MySql.MySqlClusterClient.DoPerformRequest(IRequestContext requestContext, Action`1 requestAction, Cluster`1 cluster, ICollection`1 errors, Int32 attempt, Boolean allowRetry) in c:\cement\diadocsys\_Src\DiadocSys.Net.MySql\MySql\MySqlClusterClient.cs:line 121

					   at DiadocSys.Net.MySql.MySql.MySqlClusterClient.DoPerformRequest(IRequestContext requestContext, Action`1 requestAction, Cluster`1 cluster, ICollection`1 errors, Int32 attempt, Boolean allowRetry) in c:\cement\diadocsys\_Src\DiadocSys.Net.MySql\MySql\MySqlClusterClient.cs:line 131

					   at DiadocSys.Net.MySql.MySql.MySqlClusterClient.DoPerformRequest(IRequestContext requestContext, Action`1 requestAction, Cluster`1 cluster, ICollection`1 errors, Int32 attempt, Boolean allowRetry) in c:\cement\diadocsys\_Src\DiadocSys.Net.MySql\MySql\MySqlClusterClient.cs:line 131

					   at DiadocSys.Net.MySql.MySql.MySqlClusterClient.DoPerformRequest[T](IRequestContext requestContext, Func`2 requestAction, Cluster`1 cluster, Boolean allowRetry) in c:\cement\diadocsys\_Src\DiadocSys.Net.MySql\MySql\MySqlClusterClient.cs:line 109

					   at DiadocSys.Net.MySql.DatabaseCluster.PerformRetryableWriteRequest[T](IDatabaseRequestContext context, Func`2 requestAction) in c:\cement\diadocsys\_Src\DiadocSys.Net.MySql\DatabaseCluster.cs:line 53

					   at Diadoc.Organizations.Impl.OrganizationDb.AddOrUpdateOrganization(IRequestContext requestContext, DbOrg org) in c:\cement\diadoc\_Src\Organizations\Organizations.Impl\OrganizationDb.cs:line 26

					   at Diadoc.Organizations.Impl.OrganizationUpdater.AddOrUpdateOrganization(IRequestContext requestContext, Organization org) in c:\cement\diadoc\_Src\Organizations\Organizations.Impl\OrganizationUpdater.cs:line 81

					   at Diadoc.Organizations.ActivityWatcher.ActivityByCounteragentsUpdater.UpdateActivity(IRequestContext requestContext, Guid orgId, Timestamp timestamp) in c:\cement\diadoc\_Src\App\Diadoc.Organizations.ActivityWatcher\ActivityByCounteragentsUpdater.cs:line 43

					   at Diadoc.Organizations.ActivityWatcher.ActivityByCounteragentsUpdater.Handle(RelationEvent e) in c:\cement\diadoc\_Src\App\Diadoc.Organizations.ActivityWatcher\ActivityByCounteragentsUpdater.cs:line 34

					   at DiadocSys.Storage.Framework.EventHandlerHost`1.ProcessEvent(IEntityEventHandler`1 handler, ObjectEventRecord`1 eventRecord) in c:\cement\diadoc\_Src\DiadocSys\DiadocSys.Storage\Framework\EventHandlerHost.cs:line 64 (null)

					""" ,
"""

					Diadoc.Web.Commons.HttpApplicationBase diadoc.web Unhandled exception. RequestId: b79c2b0a-1fd2-4e52-ad88-fad775254d7c, Thumbprint: bbbc712310bd55e6648642c948356834753fe9d5, ClientSystemId: diadoc.web, Locale: ru, SessionId: 00000000-0000-0000-0000-000000000000

					67d2c0a7-a436-4027-a178-d8f3ef679194

					bbbc712310bd55e6648642c948356834753fe9d5

					635495464109020721

					0

					A7C0D26736A42740A178D8F3EF679194D4BC5C42346946478FF54A0B9E9A790D, UserId: 67d2c0a7-a436-4027-a178-d8f3ef679194, Url: http://diadoc.kontur.ru/dcfeb254-aa48-4e1d-bcbf-4bd31397951b/ClaimDocumentList/RemoveDocument (null)

					System.InvalidOperationException: Cannot perform request to replica: ServiceName: claim-v2, ConnectionString: Server=dd15;Database=diadoc;Uid=claim;Pwd="Bcnht,jdfybzCenmDtotq";Unicode=True;Validate Connection=True;Default Command Timeout=30;Connection Timeout=5, ReplicaType: Master, Error: Document with id = ab79d844-7bd5-4987-a256-352f4159e4fb doesn't exist ---> System.InvalidOperationException: Document with id = ab79d844-7bd5-4987-a256-352f4159e4fb doesn't exist

					   at Diadoc.FnsClaim.ClientImpl.Storage.Database.MysqlClaimStorageV1.MysqlClaim.RemoveDocument(Guid documentId)

					   at Diadoc.FnsClaim.ClientImpl.Storage.Database.MysqlClaimStorageV1.<>c__DisplayClass13.<RemoveDocument>b__12(MysqlClaim claim)

					   at Diadoc.FnsClaim.ClientImpl.Storage.Database.MysqlClaimStorageV1.<>c__DisplayClass22.<WithClaimImpl>b__21(MysqlClaim claim)

					   at Diadoc.FnsClaim.ClientImpl.Storage.Database.MysqlClaimStorageV1.<>c__DisplayClass26`1.<WithClaimImpl>b__24(IDatabase db)

					   at DiadocSys.Net.MySql.MySql.MySqlClusterClient.TryPerformRequest(IRequestContext requestContext, Action`1 requestAction, MySqlReplica replica, ICollection`1 errors, Boolean allowRetry)

					   --- End of inner exception stack trace ---

					   at DiadocSys.Net.MySql.MySql.MySqlClusterClient.TryPerformRequest(IRequestContext requestContext, Action`1 requestAction, MySqlReplica replica, ICollection`1 errors, Boolean allowRetry)

					   at DiadocSys.Net.MySql.MySql.MySqlClusterClient.DoPerformRequest(IRequestContext requestContext, Action`1 requestAction, Cluster`1 cluster, ICollection`1 errors, Int32 attempt, Boolean allowRetry)

					   at DiadocSys.Net.MySql.DatabaseCluster.PerformNonRetryableWriteRequest(IDatabaseRequestContext context, Action`1 requestAction)

					   at Diadoc.FnsClaim.ClientImpl.Storage.Database.MysqlClaimStorageV1.WithClaimImpl[T](IRequestContext requestContext, Guid claimId, Func`2 claimFunc)

					   at Diadoc.FnsClaim.ClientImpl.Storage.Database.MysqlClaimStorageV1.WithClaimImpl(IRequestContext requestContext, Guid claimId, Action`1 claimAction)

					   at Diadoc.FnsClaim.ClientImpl.Storage.Database.MysqlClaimStorageV1.RemoveDocument(IRequestContext requestContext, Guid claimId, Guid documentId)

					   at Diadoc.FnsClaim.ClientImpl.Storage.Database.CompositeClaimStorage.<>c__DisplayClass16.<RemoveDocument>b__15(IClaimStorage storage)

					   at Diadoc.FnsClaim.ClientImpl.Storage.Database.CompositeClaimStorage.<>c__DisplayClass1.<DispatchAction>b__0(IClaimStorage storage)

					   at Diadoc.FnsClaim.ClientImpl.Storage.Database.CompositeClaimStorage.DispatchAction[T](Func`2 action)

					   at DiaDoc.WebApp.Views.Shared.Claims.List.ClaimDocumentListController.RemoveDocument(IRequestContext requestContext, Guid claimId, Guid documentId)

					   at lambda_method(Closure , ControllerBase , Object[] )

					   at System.Web.Mvc.ReflectedActionDescriptor.Execute(ControllerContext controllerContext, IDictionary`2 parameters)

					   at System.Web.Mvc.ControllerActionInvoker.InvokeActionMethod(ControllerContext controllerContext, ActionDescriptor actionDescriptor, IDictionary`2 parameters)

					   at System.Web.Mvc.ControllerActionInvoker.<>c__DisplayClass15.<InvokeActionMethodWithFilters>b__12()

					   at System.Web.Mvc.ControllerActionInvoker.InvokeActionMethodFilter(IActionFilter filter, ActionExecutingContext preContext, Func`1 continuation)

					   at System.Web.Mvc.ControllerActionInvoker.InvokeActionMethodFilter(IActionFilter filter, ActionExecutingContext preContext, Func`1 continuation)

					   at System.Web.Mvc.ControllerActionInvoker.InvokeActionMethodWithFilters(ControllerContext controllerContext, IList`1 filters, ActionDescriptor actionDescriptor, IDictionary`2 parameters)

					   at System.Web.Mvc.ControllerActionInvoker.InvokeAction(ControllerContext controllerContext, String actionName)

					   at System.Web.Mvc.Controller.ExecuteCore()

					   at System.Web.Mvc.ControllerBase.Execute(RequestContext requestContext)

					   at System.Web.Mvc.MvcHandler.<>c__DisplayClass6.<>c__DisplayClassb.<BeginProcessRequest>b__5()

					   at System.Web.Mvc.Async.AsyncResultWrapper.<>c__DisplayClass1.<MakeVoidDelegate>b__0()

					   at System.Web.HttpApplication.CallHandlerExecutionStep.System.Web.HttpApplication.IExecutionStep.Execute()

					   at System.Web.HttpApplication.ExecuteStep(IExecutionStep step, Boolean& completedSynchronously)

					""" ,
"""

					LoggerForLog4NetRuntime diadoc.web Unhandled exception on worker thread cassandraLogShipper-master-w#1

					System.Threading.ThreadAbortException: Thread was being aborted.

					   at DiadocSys.Threading.BackgroundWorkerBase.HandleWorkCompletion(IEnumerable`1 errors)

					   at DiadocSys.Threading.BackgroundWorkerBase.OnWorkCompletion(Exception[] errors)

					   at DiadocSys.Threading.CompositeBackgroundWorker.OnSingleWorkerCompletion(Int32 workerIndex, Exception error)

					   at System.Action`1.Invoke(T obj)

					   at DiadocSys.Threading.BackgroundWorkerBase.HandleWorkCompletion(IEnumerable`1 errors)

					   at DiadocSys.Threading.BackgroundWorkerBase.OnWorkCompletion(Exception[] errors)

					   at DiadocSys.Threading.CompositeBackgroundWorker.OnSingleWorkerCompletion(Int32 workerIndex, Exception error)

					   at System.Action`1.Invoke(T obj)

					   at DiadocSys.Threading.BackgroundWorkerBase.HandleWorkCompletion(IEnumerable`1 errors)

					   at DiadocSys.Threading.BackgroundWorkerBase.OnWorkCompletion(Exception[] errors)

					   at DiadocSys.Threading.BackgroundThreadWorker.RunWorker()

					""" ,
"""

					Diadoc.SLA.Impl.InMemoryIssueIndex Diadoc.SLAIndexHost Could not find issue roaming|issue:notreceivedroamingreceipt|operatorid:2bk|packetid:|msgid:|boxid:53317e31-9e89-4aa6-aca5-031353309a6c|metaid:32243d95-4787-4d58-a407-e1398a6d7fa3 to resolve it (null)

					""" ,
"""

					Diadoc.Registration.Auto.QualifiedCertificateOrganizationRegistrator Diadoc.CloudCryptHost Qualified certificate Thumbprint: F76A1ED3AFD044ABBC2ADCC9C429EB0C0AAE3305, Inn: 9909102221, OrgName: ФК с ОО "Текникас Реунидас, С.А." в г. Волгограде auto-registration skipped - org not found in focus (null)

					""" ,
"""

					LoggerForLog4NetRuntime diadoc.web Unhandled exception on worker thread cassandraLogShipper-master-w#1

					System.Threading.ThreadAbortException: Thread was being aborted.

					   at DiadocSys.Threading.BoundedBlockingTaskQueueMultiWorkerSlave`1.ProcessTaskBatch(List`1 taskBatch)

					   at DiadocSys.Threading.BoundedBlockingTaskQueueMultiWorkerSlave`1.DoWork()

					   at DiadocSys.Threading.BackgroundThreadWorker.RunWorker()

					""" ,
"""

					DiadocCommons.Http.Client.DiadocHttpClusterClient Diadoc.BillingHandlerHost Can't perform request 'POST /Balance/ReceiveTransaction?productId=Diadoc&transactionId=5b8026ca-11d4-4cf7-910d-3717f2cfa76b&senderId=d3597e82-57bd-476e-912e-8ac433ff89c5&recipientId=bb0f1fc9-2110-48f4-bff8-bb36915a336e&resourceId=Invoice&serviceId=exchange&count=1&createDateTicks=635495383038104941&comment=%D1%81%D1%87%D0%B5%D1%82-%D1%84%D0%B0%D0%BA%D1%82%D1%83%D1%80%D0%B0%20%E2%84%96223983%20%D0%BE%D1%82%2016.10.14%2C%20%D0%BE%D1%82%D0%BF%D1%80%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%3A%2022.10.14%2005%3A27%20%28%D0%9C%D0%A1%D0%9A%29%2C%20%D1%81%D1%83%D0%BC%D0%BC%D0%B0%3A%208577%2C66%2C%20%D1%81%D1%81%D1%8B%D0%BB%D0%BA%D0%B0%20%D0%BD%D0%B0%20%D0%B4%D0%BE%D0%BA%D1%83%D0%BC%D0%B5%D0%BD%D1%82%3A%20https%3A%2F%2Fdiadoc.kontur.ru%2FShowDocument%3FboxId%3D481f2052-17df-46d9-bc21-b0d8f02b6f2b%26messageId%3D9bc2df1b-de06-40ff-a705-090ab1fa6d8a%26entityId%3D5b8026ca-11d4-4cf7-910d-3717f2cfa76b' to replica billing2013 https://billy-api.kontur.ru/.

					Body: <empty> ClientSystemId: kansoTailReader, Authorization: skip, RequestId: d9090149-899e-40ba-b446-fb89d50343ef

					DiadocSys.Net.Http.Client.ReplicaFailedException: The operation has timed out ---> System.Net.WebException: The operation has timed out

					   at System.Net.HttpWebRequest.GetResponse()

					   at DiadocSys.Net.Http.Client.HttpClient.GetResponse(HttpEndPoint endPoint, IHttpRequest request) in c:\cement\diadocsys\_Src\DiadocSys.Net.Http\Client\HttpClient.cs:line 35

					   --- End of inner exception stack trace ---

					   at DiadocSys.Net.Http.Client.HttpClient.GetResponse(HttpEndPoint endPoint, IHttpRequest request) in c:\cement\diadocsys\_Src\DiadocSys.Net.Http\Client\HttpClient.cs:line 49

					   at DiadocSys.Net.Http.Client.HttpClusterClient.TryGetResponse(IHttpRequest request, HttpReplica replica, ICollection`1 errors) in c:\cement\diadocsys\_Src\DiadocSys.Net.Http\Client\HttpClusterClient.cs:line 91

					""" ,
"""

					Diadoc.App.Common.Tasks.DiadocRabbitClusterClient DC.Google.Handlers Can not dequeue (null)

					RabbitMQ.Client.Exceptions.OperationInterruptedException: The AMQP operation was interrupted: AMQP close-reason, initiated by Application, code=0, text="null BasicDeliveryEventArgs", classId=0, methodId=0, cause=

					   at DiadocSys.Net.Rabbit.RabbitQueue`1.TryDequeue(Action`1 processEvent, Nullable`1 timeout) in c:\Work\git.skbkontur.ru\diadoc\diadocsys\_Src\DiadocSys.Net.Rabbit\RabbitQueue.cs:line 50

					""" ,
"""

					DiadocCommons.Focus.FocusClient Diadoc.CounteragentsDomainHost No orgs with INN 5047040727 and KPP  found in Focus (null)

					""" ,
"""

					System.Action DC.Google.Daemon Try #1 failed, retry after 1000ms: Renci.SshNet.Common.SshConnectionException: An established connection was aborted by the software in your host machine.

					   at Renci.SshNet.Session.WaitHandle(WaitHandle waitHandle) in c:\Work\Diadoc\Ssh\SshSrc\Renci.SshClient\Renci.SshNet\Session.cs:line 640

					   at Renci.SshNet.PrivateKeyAuthenticationMethod.Authenticate(Session session) in c:\Work\Diadoc\Ssh\SshSrc\Renci.SshClient\Renci.SshNet\PrivateKeyAuthenticationMethod.cs:line 86

					   at Renci.SshNet.ConnectionInfo.Authenticate(Session session) in c:\Work\Diadoc\Ssh\SshSrc\Renci.SshClient\Renci.SshNet\ConnectionInfo.cs:line 420

					   at Renci.SshNet.Session.Connect() in c:\Work\Diadoc\Ssh\SshSrc\Renci.SshClient\Renci.SshNet\Session.cs:line 558

					   at Renci.SshNet.BaseClient.Connect() in c:\Work\Diadoc\Ssh\SshSrc\Renci.SshClient\Renci.SshNet\BaseClient.cs:line 119

					   at DC.Core.ObstinateCall.Call(Action action, Func`2 isExceptionRetriable, Int32 retries, Int32 pauseBetweenCallsMilliseconds, Action beforeRetry) in d:\BuildAgent\work\diadoc-connector-build\_Src\Core\Common\DC.Core\ObstinateCall.cs:line 32 (null)

					""" ,
"""

					Diadoc.LiveIndex.Impl.Http.GetHandler Diadoc.LiveIndexHost Too long request! Timeout: 10000 ms; Elaplsed: 10028.0064 ms; Request: BoxId: 8fd0af8a-be93-4c70-91b5-ccd476ef1cb5; LetterIds: 03f8c61a-acfc-482e-9f80-32189eacd896, 11dfef64-b42d-41c9-abdb-c76692c0b89b, 271a50f6-0269-42de-af6b-3bf4eecacc60, b0fd8bf2-88ad-4644-b2ef-f2b3ea446acd, 868e5712-f5e4-4f0e-b396-6dd86e182c82, 620b593a-4e14-463e-a528-82b0476ba3e1, 9df5375f-b1f6-495d-b4b9-3b1314354efa, 2ed63c2f-5953-4bfc-9d6e-041eb3077d3f, 08a3c3f7-e9d8-429e-8987-82fee40772cd, 1a875223-9ac8-4305-b87b-1994bb4f3c94, eedf6f75-5084-4df6-b16d-1715a999296c, 81c47014-a4c6-4a94-90c9-7c18ec9cca2f, 63011fd3-1915-458a-9cfa-9b40267a8438, b20a13d7-9732-4b56-970b-5e3e63f21f60, 01b671c3-c6ef-4955-8d37-5e787bf8615a, 39b4867a-89a6-4c59-a1bf-c2f308af07d7, 3ffc24ce-ef30-4e4a-9960-6a2e5fc31062, 6e207c2f-2fec-4140-aab4-6056d775cf4c, f5303bea-fb93-4a7f-bd3c-3f6e868513d5, f76a16ff-e35f-4d03-a05d-fa8f93941c72, d55f9d14-2bf6-40d1-bc0a-3296d61e5549, d16d83cb-f447-43b2-b650-ba8916dd1766, 90fc4c4c-c50f-4b0a-a406-1c00734a97ac, ad8fd62c-a839-47d6-897f-244c8f9aa67e, 73a21919-8045-4fdf-8bda-88db5562a797, 6249d794-9002-4aea-a17a-65de8db8e2cd, 0c770c81-296b-4db2-bfe3-9c661bf45e02, 9b030e51-c40b-4e56-80a2-0f12d2582642, bcadfc8e-4e11-4ba5-bda5-4db678475118, 2f31f11f-d624-4e0d-93ed-03a75fecca1f, 234d96be-f53b-4580-944b-369bce0665a1, 104d2899-6734-496b-9dc2-90466ae61a23, f4612ca3-e51c-40a1-9afa-1d9464f32368, 278bd474-7ef1-47b4-a832-89a4ed35654b, 0250b444-3ea1-4a0d-93d5-436c111fb6aa, 07aaf8b4-16f9-4e8d-a1bb-403029c77ff8, 42d70aaa-d261-4fa0-92ef-27b09d3168d0, 9b1dba97-25d8-4feb-8d55-67994974234d, ef74c6fa-cc17-4ef7-9dc6-9e6af26589ef, e6cbaded-646c-47bc-ac6b-179bc485de18, c7b9c443-aaa2-4da0-81ff-2bd082d2efd4, 4130bc05-715c-4fb7-aebf-6a35000a2783, 3bf5bac8-c68c-492b-af07-fc0f4438b06a, d8f8ed44-7a9f-4e08-898c-02e43e51f71d, f87d2ea3-ea21-45f4-b65e-2044bae9d978, dd2ec626-196d-40ae-8b6b-8c0c55ca6584, a40dfd28-e227-42c8-9c13-45e6ea98af65, 88feab3c-c1ae-46b6-b349-7dba8678deb6, a96665fb-696f-4d3e-9252-7b908e3d5a9f, 099fd9ef-9e85-40cc-8228-d7b62bc9eb13, 6d41f33c-8289-432a-968e-f6ebc574b309, 6346396e-220d-45a1-bce1-251f341834a9, e226b0ff-6b50-4a81-9b13-4a5cc56c450e, d01b65fb-f242-4409-aded-cd45d8f7b6f4, f6e35c83-6b6f-4a05-8224-68584ed637f4, 86193d13-9223-4d20-9e8d-69abd2e3ec9b, 9975cd46-c2b9-4c5f-b362-f863725da3c8, 1e7225a6-9b23-42cf-bd1a-8f2d3d8ab70e, 066599e6-4053-4c90-a4ea-7bdfb6126a2c, 6b95ce62-a7ea-47c3-a29b-6105d4f4c189, 6149073b-82a3-41f7-b9bc-4bace75865fc, 34c1c3f3-3e6d-4ad3-9ce5-53245fd6be38, 283b6c04-6ff2-4979-9416-31345498ab97, ef0cb6f0-6f01-496c-8f10-c45c64f87afd, 9530b862-352b-457c-be39-f29c7296691e, 2d2493fd-d203-4deb-8fc4-223dbfd6b319, ad7239b4-23bb-4973-87d4-6dd04b2a26b0, 5d3752ed-e9d7-4bac-856e-230f016c25eb, f692756d-7263-4c10-b751-42f8095b63d5, 7a179513-921d-4ae6-bb81-d2ce0ae2633b, bf62c3fe-b920-4dfe-bb07-4edb5523f731, 2aab53e3-a9a3-4190-bc23-0bbdf261bbab, 53c0770e-0b32-419a-a3e2-a411b06c6d3d, 4c318012-fd40-41f8-b2ed-432db42ab574, 19224b6d-2a58-4525-84b1-9ac248efaa27, f38b526b-9636-4a39-ac3c-542628c9abec, c51b0a34-b956-45b3-813b-a40a12306fcf, d1b045fb-c0c2-4ab4-a8cc-ec9c2c4adc5b, 75cad135-a62c-43f7-ab33-d087347bf593, 442e4074-84de-4d61-b947-be3249c4b8b3, 3ca37a50-7c23-4075-8bb4-37d9181d9087, d0ae94af-8295-4ed4-a382-041cc12f0962, b2ca41c5-cde9-4d9d-a862-15dcb822cc9a, a126e331-0b1e-44a1-bf55-f6fe6ff5819b, 06bbd2e7-e8fb-4234-bba0-8d283c7134d6, 7de43421-95a8-432a-ae35-f85316e94b2d, 4257b314-c315-44bf-9d62-404ffb5fde5e, 4520f06d-3a62-4bf0-8094-8cc85db2dcc1, d70838ea-ec18-4be0-880a-4fec7975eb14, 617b0b96-7230-4ca7-88b0-201620ab1c8f, 5771d283-03fe-4859-a18b-dfed25d428dc, adad0f58-a413-4afa-a2c1-3b28a31e7fd2, 6d09026e-e9ac-4399-ac18-4b0f8511ba05, fa55aa13-478c-49e0-a4a9-adfe561ce1b3, 9eb96311-fbc9-4381-8eb5-740788dcf209, 86839b38-16ba-4c70-a620-fbe557cf3bab, 22dd7a26-f9a0-47c6-95a7-f39ff53d9d47, 000c2891-802c-4c66-b353-acbf32347612, 9c7674fb-d9ca-4f48-9de2-98aae42dd403, e6e2e1f4-e5ab-49a2-8595-c6d990e2bf3f (null)

					""" ,
"""

					System.Action DC.Api Try #1 failed, retry after 1000ms: KonturEdiApi.HttpClient.HttpClientException: Request for url 'https://edi-api.kontur.ru/V1/Boxes/GetBoxesInfo' failed ---> System.Net.WebException: The operation has timed out

					   at System.Net.HttpWebRequest.GetResponse()

					   at KonturEdiApi.HttpClient.WebExtensions.GetWebResponse(WebRequest request) in d:\Projects\catalogue\EDI\API.Client.New\WebExtensions.cs:line 24

					   --- End of inner exception stack trace ---

					   at KonturEdiApi.HttpClient.WebExtensions.GetWebResponse(WebRequest request) in d:\Projects\catalogue\EDI\API.Client.New\WebExtensions.cs:line 30

					   at KonturEdiApi.HttpClient.KonturEdiApiHttpClient.MakeGetRequest[TResult](Uri requestUri, String authToken) in d:\Projects\catalogue\EDI\API.Client.New\KonturEdiApiHttpClient.cs:line 116

					   at DC.Core.ObstinateCall.<>c__DisplayClass1`1.<Call>b__0() in d:\BuildAgent\work\diadoc-connector-build\_Src\Core\Common\DC.Core\ObstinateCall.cs:line 15

					   at DC.Core.ObstinateCall.Call(Action action, Func`2 isExceptionRetriable, Int32 retries, Int32 pauseBetweenCallsMilliseconds, Action beforeRetry) in d:\BuildAgent\work\diadoc-connector-build\_Src\Core\Common\DC.Core\ObstinateCall.cs:line 32 (null)

					""" ,
"""

					LoggerForLog4NetRuntime diadoc.web Unhandled exception on worker thread CassandraReplicaStateProvider-CassandraAppender

					System.Threading.ThreadAbortException: Thread was being aborted.

					   at System.Threading.WaitHandle.WaitOneNative(SafeHandle waitableSafeHandle, UInt32 millisecondsTimeout, Boolean hasThreadAffinity, Boolean exitContext)

					   at System.Threading.WaitHandle.InternalWaitOne(SafeHandle waitableSafeHandle, Int64 millisecondsTimeout, Boolean hasThreadAffinity, Boolean exitContext)

					   at System.Threading.WaitHandle.WaitOne(TimeSpan timeout, Boolean exitContext)

					   at DiadocSys.Threading.BackgroundWorkerBase.WaitForStopSignal(TimeSpan timeout)

					   at DiadocSys.Threading.IterativeBackgroundThreadWorker.DoWork()

					   at DiadocSys.Threading.BackgroundThreadWorker.RunWorker()

					""" ,
"""

					DiadocCommons.Redis.DiadocRedisClusterClient Diadoc.KeNotificationHandlerHost BookSleeve.RedisConnection error. EndPoint: 192.168.52.12:6379, Cause: Invalid inbound stream (null)

					System.ObjectDisposedException: Cannot access a disposed object.

					Object name: 'System.Net.Sockets.Socket'.

					   at System.Net.Sockets.Socket.ReceiveAsync(SocketAsyncEventArgs e)

					   at BookSleeve.RedisConnectionBase.ReadMoreAsync() in d:\Dev\BookSleeve\BookSleeve\RedisConnectionBase.cs:line 613

					   at BookSleeve.RedisConnectionBase.ReadReplyHeader() in d:\Dev\BookSleeve\BookSleeve\RedisConnectionBase.cs:line 939

					""" ,
"""

					Diadoc.Billing.Impl.BillingService diadoc.web billingClient.CreateDefaultAccount() failed for inn-kpp: 7724777676-772401001 (null)

					DiadocSys.Net.Http.Client.HttpClientException: ResponseStatusCode: Conflict

					RequestUrl: https://billy-api.kontur.ru/Groups/FindOrRegister?productId=Diadoc&inn=7724777676&kpp=772401001&name=Общество с ограниченной ответственностью "ПСК МОССТРОЙМОНТАЖ"

					Conflict: {"validations":[{"value":"Group for 7724777676.772401001 already exists. It occupied by 7724777676.772401001 (f452db18-8073-4e4c-8b4b-c4ae31e4fc36)."},{"value":"Group for 7724777676.772401001 already exists. It occupied by f452db18-8073-4e4c-8b4b-c4ae31e4fc36."}]}

					   at DiadocSys.Net.Http.Client.HttpResponseExtensions.CheckStatusCode(IHttpResponse response, HttpStatusCode[] allowedStatusCodes)

					   at DiadocSys.Net.Http.Client.HttpClusterClientExtensions.PerformHttpRequest[TResponse](IHttpClusterClient httpClient, IHttpRequest httpRequest, Nullable`1 clientId, Func`2 parseResponse)

					   at DiadocSys.Net.Http.Client.HttpClusterClientExtensions.PerformJsonHttpRequest[TResponse](IHttpClusterClient httpClient, IHttpRequest httpRequest, Nullable`1 clientId)

					   at DiadocSys.Net.Http.Client.HttpClusterClientExtensions.PerformJsonHttpRequest[TResponse](IHttpClusterClient httpClient, IRequestContext requestContext, String queryString, HttpMethod httpMethod, Nullable`1 clientId)

					   at DiadocCommons.Portal.Billing.BillingClient.CreateDefaultAccount(IRequestContext requestContext, String inn, String kpp, String name)

					   at Diadoc.Billing.Impl.BillingService.TryCreateDefaultAccount(IRequestContext context, String inn, String kpp, String name)

					""" ,
"""

					Diadoc.FnsClaim.ClientImpl.Storage.Database.ClaimedDocumentDatabaseCluster Diadoc.FnsClaimHost Cannot perform request to replica: ServiceName: claim-v2, ConnectionString: Server=dd15;Database=diadoc;Uid=claim;Pwd="Bcnht,jdfybzCenmDtotq";Unicode=True;Validate Connection=True;Default Command Timeout=30;Connection Timeout=5, ReplicaType: Master, Error: Sequence contains no matching element RequestId: 70b704c9-6767-4059-8cc2-6b93e106e6a0, Thumbprint: cf45703cb4bea28be7849ee6cd19ade6f89f14ee, ClientSystemId: diadoc.web, Locale: ru, SessionId: 00000000-0000-0000-0000-000000000000

					52ae5563-1ff1-4d36-a9b9-4a68fc42d588

					cf45703cb4bea28be7849ee6cd19ade6f89f14ee

					635495477182650017

					0

					6355AE52F11F364DA9B94A68FC42D58845E6F4524709774DAC5A55C96E0B9647, UserId: 52ae5563-1ff1-4d36-a9b9-4a68fc42d588, ClaimID: 21a420ea-f7a7-4ad3-adfa-0b298daa9e9e, ImportID: 5a21368c-0478-4c94-b2a0-367f73492549

					System.InvalidOperationException: Sequence contains no matching element

					   at System.Linq.Enumerable.Single[TSource](IEnumerable`1 source, Func`2 predicate)

					   at Diadoc.FnsClaim.ClientImpl.Storage.Database.MysqlClaimStorageV1.MysqlClaim.GetDocument(Guid documentId) in c:\cement\diadoc\_Src\FnsClaim\Diadoc.FnsClaim.ClientImpl\Storage\Database\MysqlClaimStorageV1.cs:line 352

					   at Diadoc.FnsClaim.ClientImpl.Storage.Database.MysqlClaimStorageV1.<>c__DisplayClass1.<ReplaceDocumentImpl>b__0(MysqlClaim claim) in c:\cement\diadoc\_Src\FnsClaim\Diadoc.FnsClaim.ClientImpl\Storage\Database\MysqlClaimStorageV1.cs:line 456

					   at Diadoc.FnsClaim.ClientImpl.Storage.Database.MysqlClaimStorageV1.<>c__DisplayClass26`1.<WithClaimImpl>b__24(IDatabase db) in c:\cement\diadoc\_Src\FnsClaim\Diadoc.FnsClaim.ClientImpl\Storage\Database\MysqlClaimStorageV1.cs:line 636

					   at DiadocSys.Net.MySql.MySql.MySqlClusterClient.TryPerformRequest(IRequestContext requestContext, Action`1 requestAction, MySqlReplica replica, ICollection`1 errors, Boolean allowRetry) in c:\cement\diadocsys\_Src\DiadocSys.Net.MySql\MySql\MySqlClusterClient.cs:line 144

					""" ,
"""

					DiadocCommons.Rabbit.DiadocRabbitClusterClient Diadoc.FnsClaimHost Error while connecting to rabbitmq replica ServiceName: rabbit, EndPoint: 192.168.52.13:5672 (null)

					None of the specified endpoints were reachable

					Endpoints attempted:

					------------------------------------------------

					endpoint=amqp-0-9://192.168.52.13:5672, attempts=1

					System.TimeoutException: Connection to amqp-0-9://192.168.52.13:5672 timed out

					   at RabbitMQ.Client.Impl.SocketFrameHandler_0_9.Connect(TcpClient socket, AmqpTcpEndpoint endpoint, Int32 timeout)

					   at RabbitMQ.Client.Impl.SocketFrameHandler_0_9..ctor(AmqpTcpEndpoint endpoint, ObtainSocket socketFactory, Int32 timeout)

					   at RabbitMQ.Client.Framing.Impl.v0_9_1.ProtocolBase.CreateFrameHandler(AmqpTcpEndpoint endpoint, ObtainSocket socketFactory, Int32 timeout)

					   at RabbitMQ.Client.ConnectionFactory.FollowRedirectChain(Int32 maxRedirects, IDictionary`2 connectionAttempts, IDictionary`2 connectionErrors, AmqpTcpEndpoint[]& mostRecentKnownHosts, AmqpTcpEndpoint endpoint)

					================================================

					Stack trace:

					   at RabbitMQ.Client.ConnectionFactory.CreateConnection(Int32 maxRedirects)

					   at DiadocSys.Net.Rabbit.RabbitConnection.TryConnect(Replica replica, UInt16 heartbeat, ICollection`1 errors) in c:\cement\diadocsys\_Src\DiadocSys.Net.Rabbit\RabbitConnection.cs:line 126

					""" ,
"""

					Diadoc.Domain.RestorePasswordManager diadoc.web Invalid secret key for change password, key = B2FF4C36C440B8ACFDCB8D1AD091B35EA66154592353EBEE, exception = Newtonsoft.Json.JsonReaderException: Unexpected character encountered while parsing value: a. Path '', line 0, position 0.

					   at Newtonsoft.Json.JsonTextReader.ParseValue()

					   at Newtonsoft.Json.JsonTextReader.ReadInternal()

					   at Newtonsoft.Json.JsonTextReader.Read()

					   at Newtonsoft.Json.Serialization.JsonSerializerInternalReader.ReadForType(JsonReader reader, JsonContract contract, Boolean hasConverter)

					   at Newtonsoft.Json.Serialization.JsonSerializerInternalReader.Deserialize(JsonReader reader, Type objectType, Boolean checkAdditionalContent)

					   at Newtonsoft.Json.JsonSerializer.DeserializeInternal(JsonReader reader, Type objectType)

					   at Newtonsoft.Json.JsonConvert.DeserializeObject(String value, Type type, JsonSerializerSettings settings)

					   at Newtonsoft.Json.JsonConvert.DeserializeObject[T](String value, JsonSerializerSettings settings)

					   at Diadoc.Domain.RestorePasswordManager.TryGetSecretKeyForChangePassword(User user, String encryptedSecretKey) (null)

					""" ,
"""

					DiaDoc.WebApp.Controllers.Send.NonformalizedAttachmentModelProvider diadoc.web Document recognition error: System.NotSupportedException: Cannot recognize document (invalid format) ---> System.IndexOutOfRangeException: Index was outside the bounds of the array.

					   at System.Collections.Generic.List`1.Add(T item)

					   at NPOI.SS.Formula.Udf.AggregatingUDFFinder.Add(UDFFinder toolPack)

					   at NPOI.HSSF.UserModel.HSSFWorkbook.AddToolPack(UDFFinder toopack)

					   at FieldsRecognition.DocumentModel.Excel.ExcelModelBuilder..ctor(Stream stream)

					   at FieldsRecognition.DocumentModel.Excel.ExcelModelBuilder.BuilderFrom(Stream stream)

					   --- End of inner exception stack trace ---

					   at FieldsRecognition.DocumentModel.Excel.ExcelModelBuilder.BuilderFrom(Stream stream)

					   at DiaDoc.WebApp.Controllers.Send.NonformalizedAttachmentModelProvider.GetAttachment2Send(Byte[] fileContent, String filename, ClientContentLocation serverSideLocation)

					   at DiaDoc.WebApp.Controllers.Send.NonformalizedAttachmentModelProvider.TryGetAttachment2Send(Byte[] fileContent, String filename, ClientContentLocation serverSideLocation) (null)

					""" ,
"""

					Diadoc.TimeStampServer.Impl.CrlManagement.CrlDownloader Diadoc.TimeStampServerHost Failed to get crl from: http://www.komi-cit.ru/certsrv/cbi-gov2013.crl (null)

					DiadocSys.Net.Http.Client.HttpClientException: ResponseStatusCode: NotFound

					RequestUrl: http://www.komi-cit.ru/certsrv/cbi-gov2013.crl

					Http StatusCode: NotFound

					   at DiadocSys.Net.Http.Client.HttpResponseExtensions.CheckStatusCode(IHttpResponse response, HttpStatusCode[] allowedStatusCodes) in c:\cement\diadocsys\_Src\DiadocSys.Net.Http\Client\HttpResponseExtensions.cs:line 23

					   at Diadoc.TimeStampServer.Impl.CrlManagement.CrlDownloader.TryGetCrl(IRequestContext context, String cdpUrl) in c:\cement\diadoc\_Src\App\Diadoc.TimeStampServer.Impl\CrlManagement\CrlDownloader.cs:line 45

					""" ,
"""

					DiadocCommons.Portal.Auth.AuthServiceClient Diadoc.OvermindHost auth error from replica https://portal-services.kontur.ru/auth/identity/certificate (null)

					""" ,
"""

					LoggerForLog4NetRuntime diadoc.web Failed to process TaskBatch<LoggingEvent>[26]: log4net.Core.LoggingEvent

					log4net.Core.LoggingEvent

					log4net.Core.LoggingEvent

					log4net.Core.LoggingEvent

					log4net.Core.LoggingEvent...

					System.Threading.ThreadAbortException: Thread was being aborted.

					   at log4net.Core.LoggingEvent.GetLoggingEventData(FixFlags fixFlags)

					   at DiadocLogging.Cassandra.Shipping.LoggingEventExtensions.ConvertToLogRecord(LoggingEvent loggingEvent, Func`2 messageFormatter)

					   at DiadocLogging.Cassandra.Shipping.CassandraLogShipperWorkerSlave.DoProcessTaskBatch(List`1 taskBatch)

					   at DiadocSys.Threading.BoundedBlockingTaskQueueMultiWorkerSlave`1.ProcessTaskBatch(List`1 taskBatch)

					""" ,
"""

					DiadocCommons.Http.Server.DiadocHttpServer Diadoc.CloudCryptHost Could not process http request: Id: 6d3f0417-71a5-4337-af4a-766279d10d04, Url: http://vm-dd-ts01:15247/CloudCrypt.v1/signReceipts, Transcript:

					Headers:

					X-Diadoc-ClientTimeout: 10000

					X-Diadoc-Context-RequestId: 6d3f0417-71a5-4337-af4a-766279d10d04

					X-Diadoc-Context-ClientSystemId: diadoc.web

					X-Diadoc-Context-Locale: ru

					X-Diadoc-Context-SessionId: 00000000-0000-0000-0000-000000000000%0Ae013da98-9900-4f7c-871b-bd05d8900921%0A%0A635495315650207999%0A0%0A98DA13E000997C4F871BBD05D89009215755F5289B9D6C48952CD4F442BD49DD

					X-Diadoc-Context-UserId: e013da98-9900-4f7c-871b-bd05d8900921

					Connection: Keep-Alive

					Content-Length: 28898

					Expect: 100-continue

					Host: vm-dd-ts01:15247

					Body:

					Body-Length: 28898 (null)

					System.Net.WebException: The remote server returned an error: (500) Internal Server Error.

					   at System.Net.HttpWebRequest.GetResponse()

					   at Diadoc.CloudCrypt.Cryptography.CloudCrypt.SignWithoutConfirm(IEnumerable`1 signItems, String certificateBase64) in c:\cement\diadoc\_Src\App\Diadoc.CloudCrypt\Cryptography\CloudCrypt.cs:line 98

					   at Diadoc.CloudCrypt.Cryptography.CloudCryptClient.DoSignReceipts(List`1 items, String certificateThumbprint, String certificateBase64) in c:\cement\diadoc\_Src\App\Diadoc.CloudCrypt\Cryptography\CloudCryptClient.cs:line 107

					   at Diadoc.CloudCrypt.Cryptography.CloudCryptClient.SignReceipts(IRequestContext requestContext, String certificateThumbprint, CloudCryptFile[] files) in c:\cement\diadoc\_Src\App\Diadoc.CloudCrypt\Cryptography\CloudCryptClient.cs:line 100

					   at Diadoc.CloudCrypt.Rest.Server.CloudCryptDomain.SignReceiptsImpl(SignArgs signArgs) in c:\cement\diadoc\_Src\App\Diadoc.CloudCrypt.Rest\Server\CloudCryptDomain.cs:line 60

					   at Castle.Proxies.FuncBasedCommand`2Proxy_2.Execute_callback(SignArgs args)

					   at Castle.Proxies.Invocations.FuncBasedCommand`2_Execute_2.InvokeMethodOnTarget()

					   at Castle.DynamicProxy.AbstractInvocation.Proceed() in d:\work\16de7b8c88ab14af\src\Castle.Core\DynamicProxy\AbstractInvocation.cs:line 123

					   at Castle.DynamicProxy.AbstractInvocation.Proceed() in d:\work\16de7b8c88ab14af\src\Castle.Core\DynamicProxy\AbstractInvocation.cs:line 145

					   at Castle.Proxies.FuncBasedCommand`2Proxy_2.Execute(SignArgs args)

					   at Diadoc.Rest.Server.DomainFunc`2.Diadoc.Rest.Server.Domain.IDomainCommandInvoker.Invoke(Object args) in c:\cement\diadoc\_Src\DiadocSys\Diadoc.Rest\Server\DomainFunc.cs:line 63

					   at Diadoc.Rest.Server.Http.RestHttpHandler.ProcessCommandInvocationRequest(IHttpContext httpContext, IServerDomainNode domainNode, IRequestContext requestContext) in c:\cement\diadoc\_Src\DiadocSys\Diadoc.Rest\Server\Http\RestHttpHandler.cs:line 111

					   at Diadoc.Rest.Server.Http.RestHttpHandler.GetResponse(IHttpContext httpContext, Func`1 getResponse) in c:\cement\diadoc\_Src\DiadocSys\Diadoc.Rest\Server\Http\RestHttpHandler.cs:line 80

					   at Diadoc.Rest.Server.Http.RestHttpHandler.ProcessRequest(NameValueCollection queryString, IHttpContext httpContext) in c:\cement\diadoc\_Src\DiadocSys\Diadoc.Rest\Server\Http\RestHttpHandler.cs:line 52

					   at DiadocSys.Net.Http.Server.HttpServer.ProcessSyncRequest(IHttpContext httpContext, RequestHandlerFactory requestHandlerFactory) in c:\cement\diadocsys\_Src\DiadocSys.Net.Http\Server\HttpServer.cs:line 215

					""" ,
"""

					DiadocCommons.Http.Server.DiadocHttpServer Diadoc.DocumentsDomainHost Could not process http request: Id: 870154a8-36e7-42ff-8728-168efcc2fb8d, Url: http://192.168.52.153:48004/Documents.v1/Boxes/34654dac-e692-4f1f-b166-c529…48-7504802effbb/bilateralDocflow/createSignatureRejectionContent?execute={"comment":null}&_=1413944968408, Transcript:

					Headers:

					X-Diadoc-ClientTimeout: 10000

					X-Diadoc-Context-RequestId: 870154a8-36e7-42ff-8728-168efcc2fb8d

					X-Diadoc-Context-Thumbprint: 160cbbf81dcfdb3e9e0ebbe0899469bd8d846151

					X-Diadoc-Context-ClientSystemId: diadoc.web

					X-Diadoc-Context-Locale: ru

					X-Diadoc-Context-SessionId: 00000000-0000-0000-0000-000000000000%0A9afeb824-ca98-4600-a7de-848463ffbf83%0A160cbbf81dcfdb3e9e0ebbe0899469bd8d846151%0A635495416708848814%0A0%0A24B8FE9A98CA0046A7DE848463FFBF838F2588D4E8C602419FDD2AB5A2F63ABC

					X-Diadoc-Context-UserId: 9afeb824-ca98-4600-a7de-848463ffbf83

					Host: 192.168.52.153:48004

					Body:

					<EMPTY> (null)

					System.InvalidOperationException: Signature cannot be rejected for document DocflowEntityType: TrustConnectionRequestDocument, Entity: Attachment/TrustConnectionRequest Id: 429c83ac-e7cf-479d-ac48-7504802effbb, ParentEntityId:, AttachmentFileName: Соглашение о документообороте в электронном виде.pdf, KansoLocation: 6:371243617578:163745:Guid: 476e9cd2-590d-11e4-8000-b947d6126c9f, Timestamp: Ticks: 635494842295835858, DateTime: 2014-10-21 10:30:29Z

					EntityId:429c83ac-e7cf-479d-ac48-7504802effbb

					EntityType:Attachment

					AttachmentType:TrustConnectionRequest

					AttachmentFileName:Соглашение о документообороте в электронном виде.pdf

					AttachmentFileSize:163745

					RecipientSignatureRequest:

					CreationTimestamp:Ticks: 635494842296017048, DateTime: 2014-10-21 10:30:29Z

					IsRead:

					, LetterMetaSlice: RootEntity: Attachment/TrustConnectionRequest Id: 429c83ac-e7cf-479d-ac48-7504802effbb, ParentEntityId:, AttachmentFileName: Соглашение о документообороте в электронном виде.pdf, KansoLocation: 6:371243617578:163745:Guid: 476e9cd2-590d-11e4-8000-b947d6126c9f, Timestamp: Ticks: 635494842295835858, DateTime: 2014-10-21 10:30:29Z

					EntityId:429c83ac-e7cf-479d-ac48-7504802effbb

					EntityType:Attachment

					AttachmentType:TrustConnectionRequest

					AttachmentFileName:Соглашение о документообороте в электронном виде.pdf

					AttachmentFileSize:163745

					RecipientSignatureRequest:

					CreationTimestamp:Ticks: 635494842296017048, DateTime: 2014-10-21 10:30:29Z

					IsRead:

					, LetterMeta: LetterMeta 70e745b5-401d-409c-bfa7-19c73f4f7f49, Timestamp: Ticks: 635494842299435641, DateTime: 2014-10-21 10:30:29Z, Box: 34654dac-e692-4f1f-b166-c529d4bebeae

					To:34654dac-e692-4f1f-b166-c529d4bebeae

					From:ea01b5c8-edfd-4048-bab7-065f33d586b8

					Sent:Ticks: 635494842296017048, DateTime: 2014-10-21 10:30:29Z

					CreatedBySystem:diadoc.api:RtUral-9bddf187-24d1-4e47-9149-f0a01a113da2



					   at Diadoc.Documents.Rest.Domain.CreateSignatureRejectionContentCommand.Execute(CreateSignatureRejectionArgs args) in c:\cement\diadoc\_Src\Documents\Diadoc.Documents.Rest\Domain\CreateSignatureRejectionContentCommand.cs:line 37

					   at Castle.Proxies.Invocations.CreateSignatureRejectionContentCommand_Execute.InvokeMethodOnTarget()

					   at Castle.DynamicProxy.AbstractInvocation.Proceed() in d:\work\16de7b8c88ab14af\src\Castle.Core\DynamicProxy\AbstractInvocation.cs:line 123

					   at Castle.DynamicProxy.AbstractInvocation.Proceed() in d:\work\16de7b8c88ab14af\src\Castle.Core\DynamicProxy\AbstractInvocation.cs:line 145

					   at Castle.Proxies.CreateSignatureRejectionContentCommandProxy.Execute(CreateSignatureRejectionArgs args)

					   at Diadoc.Rest.Server.DomainFunc`2.Diadoc.Rest.Server.Domain.IDomainCommandInvoker.Invoke(Object args) in c:\cement\diadoc\_Src\DiadocSys\Diadoc.Rest\Server\DomainFunc.cs:line 63

					   at Diadoc.Rest.Server.Http.RestHttpHandler.ProcessCommandInvocationRequest(IHttpContext httpContext, IServerDomainNode domainNode, IRequestContext requestContext) in c:\cement\diadoc\_Src\DiadocSys\Diadoc.Rest\Server\Http\RestHttpHandler.cs:line 111

					   at Diadoc.Rest.Server.Http.RestHttpHandler.GetResponse(IHttpContext httpContext, Func`1 getResponse) in c:\cement\diadoc\_Src\DiadocSys\Diadoc.Rest\Server\Http\RestHttpHandler.cs:line 80

					   at Diadoc.Rest.Server.Http.RestHttpHandler.ProcessRequest(NameValueCollection queryString, IHttpContext httpContext) in c:\cement\diadoc\_Src\DiadocSys\Diadoc.Rest\Server\Http\RestHttpHandler.cs:line 47

					   at DiadocSys.Net.Http.Server.HttpServer.ProcessSyncRequest(IHttpContext httpContext, RequestHandlerFactory requestHandlerFactory) in c:\cement\diadocsys\_Src\DiadocSys.Net.Http\Server\HttpServer.cs:line 215

					""" ,
"""

					DiadocSys.Tasks.TiedTasks.TiedTaskHandler Diadoc.BillingHandlerHost System.InvalidOperationException: BillingAccountId is not set for org: 17d00378-634a-4791-abf5-1a7b370bc9f8

					   at Diadoc.Billing.Impl.Transactions.BillingTaskHandler.GetCounteragentAccountId(IRequestContext requestContext, Guid counteragentOrgId) in c:\cement\diadoc\_Src\Billing\Diadoc.Billing\Impl\Transactions\BillingTaskHandler.cs:line 35

					   at Diadoc.Billing.Impl.Transactions.BillingTaskHandler.Process(BillingDocumentData task, ITiedTaskContext taskContext) in c:\cement\diadoc\_Src\Billing\Diadoc.Billing\Impl\Transactions\BillingTaskHandler.cs:line 26

					   at DiadocSys.Tasks.TiedTasks.Simple.TiedTaskSimpleProcessorBase`2.Process(TiedTaskQueueItem task, TiedTaskResult[] childResults, ITiedTaskContext taskContext) in c:\cement\diadoc\_Src\DiadocSys\DiadocSys.Tasks\TiedTasks\Simple\TiedTaskSimpleProcessorBase.cs:line 88

					   at DiadocSys.Tasks.TiedTasks.TiedTaskHandler.Process(TiedTaskQueueItem task, TiedTaskResult[] childTaskResults, IRequestContext requestContext, Boolean isCancelled) in c:\cement\diadoc\_Src\DiadocSys\DiadocSys.Tasks\TiedTasks\TiedTaskHandler.cs:line 168 ClientSystemId: kansoTailReader, Authorization: skip, RequestId: 0fa253dc-8f20-4f3a-94bf-1499e339a1a9

					""" ,
"""

					System.Action DC.Api Try #1 failed, retry after 1000ms: KonturEdiApi.HttpClient.HttpClientException: Request for url 'https://edi-api.kontur.ru/V1/Boxes/GetBoxesInfo' failed ---> System.Net.WebException: Unable to connect to the remote server ---> System.Net.Sockets.SocketException: A connection attempt failed because the connected party did not properly respond after a period of time, or established connection failed because connected host has failed to respond 46.17.200.218:443

					   at System.Net.Sockets.Socket.DoConnect(EndPoint endPointSnapshot, SocketAddress socketAddress)

					   at System.Net.ServicePoint.ConnectSocketInternal(Boolean connectFailure, Socket s4, Socket s6, Socket& socket, IPAddress& address, ConnectSocketState state, IAsyncResult asyncResult, Exception& exception)

					   --- End of inner exception stack trace ---

					   at System.Net.HttpWebRequest.GetResponse()

					   at KonturEdiApi.HttpClient.WebExtensions.GetWebResponse(WebRequest request) in d:\Projects\catalogue\EDI\API.Client.New\WebExtensions.cs:line 24

					   --- End of inner exception stack trace ---

					   at KonturEdiApi.HttpClient.WebExtensions.GetWebResponse(WebRequest request) in d:\Projects\catalogue\EDI\API.Client.New\WebExtensions.cs:line 30

					   at KonturEdiApi.HttpClient.KonturEdiApiHttpClient.MakeGetRequest[TResult](Uri requestUri, String authToken) in d:\Projects\catalogue\EDI\API.Client.New\KonturEdiApiHttpClient.cs:line 116

					   at DC.Core.ObstinateCall.<>c__DisplayClass1`1.<Call>b__0() in d:\BuildAgent\work\diadoc-connector-build\_Src\Core\Common\DC.Core\ObstinateCall.cs:line 15

					   at DC.Core.ObstinateCall.Call(Action action, Func`2 isExceptionRetriable, Int32 retries, Int32 pauseBetweenCallsMilliseconds, Action beforeRetry) in d:\BuildAgent\work\diadoc-connector-build\_Src\Core\Common\DC.Core\ObstinateCall.cs:line 32 (null)

					""" ,
"""

					LoggerForLog4NetRuntime diadoc.web CassandraAppender will use the following settings: {"MaxQueueSize":2147483647,"LogEventEnqueueTimeout":"00:03:00","WorkersCount":4,"LogMessageTtl":"30.00:00:00","LogsKeySpace":"DiadocLogs","CassandraClusterClientSettings":{"ReplicaStateProviderCheckInterval":"00:00:10","ConnectionPoolSettings":{"MaxConnectionsPerEndPoint":50,"ConnectionTtl":"00:10:00","RequestTimeout":"00:01:00"}},"WorkerSettings":{"ConversionPattern":"%m %property{context}","MaxShippingBatchSize":256,"MaxShippingDelay":"00:00:05","MinTaskDequeueTimeout":"00:00:00.1000000"}}

					""" ,
"""

					WebAdminApp.CheckPermissionActionFilter diadoc.webadmin Access denied to Monitor.Index for user: a18f3751-f88d-40f5-a4bf-70556f0575ad (null)

					""" ,
"""

					DiadocCommons.Rabbit.DiadocRabbitClusterClient Diadoc.FnsClaimHost Can not dispose connection (null)

					System.IO.EndOfStreamException: Heartbeat missing with heartbeat == 5 seconds

					   at RabbitMQ.Client.Impl.ConnectionBase.System.IDisposable.Dispose()

					   at DiadocSys.Net.Rabbit.RabbitConnection.Disconnect() in c:\cement\diadocsys\_Src\DiadocSys.Net.Rabbit\RabbitConnection.cs:line 102

					""" ,
"""

					DiadocCommons.Rabbit.DiadocRabbitClusterClient Diadoc.FnsClaimHost Error while connecting to rabbitmq replica ServiceName: rabbit, EndPoint: 192.168.52.12:5672 (null)

					None of the specified endpoints were reachable

					Endpoints attempted:

					------------------------------------------------

					endpoint=amqp-0-9://192.168.52.12:5672, attempts=1

					System.NotSupportedException: Stream does not support writing.

					   at System.IO.BufferedStream.EnsureCanWrite()

					   at System.IO.BufferedStream.Write(Byte[] array, Int32 offset, Int32 count)

					   at System.IO.BinaryWriter.Write(Byte[] buffer)

					   at RabbitMQ.Client.Impl.SocketFrameHandler_0_9.SendHeader()

					   at RabbitMQ.Client.Impl.ConnectionBase.StartAndTune()

					   at RabbitMQ.Client.Framing.Impl.v0_9_1.Connection.Open(Boolean insist)

					   at RabbitMQ.Client.Impl.ConnectionBase..ctor(ConnectionFactory factory, Boolean insist, IFrameHandler frameHandler)

					   at RabbitMQ.Client.Framing.Impl.v0_9_1.ProtocolBase.CreateConnection(ConnectionFactory factory, Boolean insist, IFrameHandler frameHandler)

					   at RabbitMQ.Client.ConnectionFactory.FollowRedirectChain(Int32 maxRedirects, IDictionary`2 connectionAttempts, IDictionary`2 connectionErrors, AmqpTcpEndpoint[]& mostRecentKnownHosts, AmqpTcpEndpoint endpoint)

					================================================

					Stack trace:

					   at RabbitMQ.Client.ConnectionFactory.CreateConnection(Int32 maxRedirects)

					   at DiadocSys.Net.Rabbit.RabbitConnection.TryConnect(Replica replica, UInt16 heartbeat, ICollection`1 errors) in c:\cement\diadocsys\_Src\DiadocSys.Net.Rabbit\RabbitConnection.cs:line 126

					""" ,
"""

					Diadoc.Roaming.Impl.Handlers.ToRoaming.ToRoamingTaskHandler Diadoc.Roaming.RoamingHandlerHost Diadoc.Api.Http.HttpClientException: BaseUrl=https://courier-roaming.esphere.ru:443, PathAndQuery=/, AdditionalMessage=, StatusCode= ---> System.Net.WebException: Unable to connect to the remote server ---> System.Net.Sockets.SocketException: A connection attempt failed because the connected party did not properly respond after a period of time, or established connection failed because connected host has failed to respond 212.65.87.200:443

					   at System.Net.Sockets.Socket.DoConnect(EndPoint endPointSnapshot, SocketAddress socketAddress)

					   at System.Net.ServicePoint.ConnectSocketInternal(Boolean connectFailure, Socket s4, Socket s6, Socket& socket, IPAddress& address, ConnectSocketState state, IAsyncResult asyncResult, Exception& exception)

					   --- End of inner exception stack trace ---

					   at System.Net.HttpWebRequest.GetRequestStream(TransportContext& context)

					   at System.Net.HttpWebRequest.GetRequestStream()

					   at Diadoc.Api.Http.HttpClient.PrepareWebRequest(HttpRequest request) in c:\dev\diadocsdk\C#\DiadocApi\Http\HttpClient.cs:line 163

					   at Diadoc.Api.Http.HttpClient.PerformHttpRequest(HttpRequest request, HttpStatusCode[] allowedStatusCodes) in c:\dev\diadocsdk\C#\DiadocApi\Http\HttpClient.cs:line 92

					   --- End of inner exception stack trace ---

					   at Diadoc.Api.Http.HttpClient.PerformHttpRequest(HttpRequest request, HttpStatusCode[] allowedStatusCodes) in c:\dev\diadocsdk\C#\DiadocApi\Http\HttpClient.cs:line 120

					   at Diadoc.Roaming.Impl.Handlers.ToRoaming.PacketSender.Send(IRequestContext requestContext, Byte[] packetData, String packetId, Uri destination, String operatorId, String logTag) in c:\cement\diadoc\_Src\Roaming\Diadoc.Roaming.Impl\Handlers\ToRoaming\PacketSender.cs:line 59

					   at Diadoc.Roaming.Impl.Handlers.ToRoaming.ToRoamingTaskHandler.Process(ToRoamingTask task, ITiedTaskContext taskContext) in c:\cement\diadoc\_Src\Roaming\Diadoc.Roaming.Impl\Handlers\ToRoaming\ToRoamingTaskHandler.cs:line 34 ClientSystemId: diadoc.roaming, Authorization: skip, RequestId: 2f32c921-7e79-4fa8-b3f2-d098b4f6c703

					""" ,
"""

					PotentialCounteragentsRate.Program PotentialCounteragentsRate Failed to start service (null)

					RoboContainer.Core.ContainerException: Не найден файл настроек settings/topology/statistics.

					Get IStatisticsMysqlClusterClient

						Constructing StatisticsMysqlClusterClient

							Get IReplicaClientIdProvider

								Constructing StaticReplicaClientIdProvider

								Constructed StaticReplicaClientIdProvider

							Get IRecentWritersList

								Constructing RecentWritersList

								Constructed RecentWritersList

					 ---> RoboContainer.Core.ContainerException: Не найден файл настроек settings/topology/statistics. ---> System.IO.FileNotFoundException: Не найден файл настроек settings/topology/statistics.

					   at Diadoc.Commons.SettingsFile`1.ReloadSettings() in c:\Projects\diadoc\_Src\Common\Diadoc.Commons\SettingsFile.cs:line 38

					   at Diadoc.Commons.SettingsFile`1.GetSettings() in c:\Projects\diadoc\_Src\Common\Diadoc.Commons\SettingsFile.cs:line 28

					   at Diadoc.Protocols.Topology.MySql.MySqlTopologySettings.GetFreshAddresses() in c:\Projects\diadoc\_Src\Transport\Diadoc.Protocols.Topology\MySql\MySqlTopologySettings.cs:line 25

					   at Diadoc.Protocols.Database.MySql.MysqlClusterClient..ctor(Func`1 getReplicas, Boolean runRequestSpy) in c:\Projects\diadoc\_Src\Storage\Diadoc.Protocols.Database\MySql\MysqlClusterClient.cs:line 48

					   at Diadoc.Protocols.Database.MySql.StatisticsMysqlClusterClient..ctor(IReplicaClientIdProvider replicaClientIdProvider, IRecentWritersList recentWritersList) in c:\Projects\diadoc\_Src\Storage\Diadoc.Protocols.Database\MySql\StatisticsMysqlClusterClient.cs:line 12

					   --- End of inner exception stack trace ---

					   at RoboContainer.Impl.ByConstructorInstanceFactory.TryCreatePluggable(Container container, Type pluginToCreate, String[] requiredContracts, Func`2 initializeJustCreatedObject) in d:\BuildAgent\work\cc82e7f9f0d8d5c1\RoboContainer\Impl\ByConstructorInstanceFactory.cs:line 48

					   at RoboContainer.Impl.AbstractInstanceFactory.TryConstruct(IConstructionLogger logger, Type typeToCreate, String[] requiredContracts, Func`2 initializeJustCreatedObject) in d:\BuildAgent\work\cc82e7f9f0d8d5c1\RoboContainer\Impl\AbstractInstanceFactory.cs:line 50

					   at RoboContainer.Impl.AbstractInstanceFactory.TryGetOrCreate(IConstructionLogger logger, Type typeToCreate, String[] requiredContracts, Func`2 initializeJustCreatedObject) in d:\BuildAgent\work\cc82e7f9f0d8d5c1\RoboContainer\Impl\AbstractInstanceFactory.cs:line 31

					   at RoboContainer.Impl.ConfiguredPluggableExtensions.TryGetOrCreate(IConfiguredPluggable pluggable, IConstructionLogger logger, Type pluginType, String[] requiredContracts, IContainerConfiguration configuration) in d:\BuildAgent\work\cc82e7f9f0d8d5c1\RoboContainer\Impl\IConfiguredPluggable.cs:line 38

					   at RoboContainer.Core.Container.<>c__DisplayClassc.<PlainGetAll>b__8(IConfiguredPluggable c) in d:\BuildAgent\work\cc82e7f9f0d8d5c1\RoboContainer\Core\Container.cs:line 178

					   at System.Linq.Enumerable.WhereSelectListIterator`2.MoveNext()

					   at System.Linq.Enumerable.WhereEnumerableIterator`1.MoveNext()

					   at System.Collections.Generic.List`1..ctor(IEnumerable`1 collection)

					   at System.Linq.Enumerable.ToList[TSource](IEnumerable`1 source)

					   at RoboContainer.Core.Container.PlainGetAll(Type pluginType, String[] requiredContracts) in d:\BuildAgent\work\cc82e7f9f0d8d5c1\RoboContainer\Core\Container.cs:line 177

					   at RoboContainer.Core.Container.GetAll(Type pluginType, String[] requiredContracts) in d:\BuildAgent\work\cc82e7f9f0d8d5c1\RoboContainer\Core\Container.cs:line 110

					   --- End of inner exception stack trace ---

					   at RoboContainer.Core.Container.GetAll(Type pluginType, String[] requiredContracts) in d:\BuildAgent\work\cc82e7f9f0d8d5c1\RoboContainer\Core\Container.cs:line 116

					   at RoboContainer.Core.Container.Get(Type pluginType, String[] requiredContracts) in d:\BuildAgent\work\cc82e7f9f0d8d5c1\RoboContainer\Core\Container.cs:line 88

					   at RoboContainer.Core.Container.Get[TPlugin](String[] requiredContracts) in d:\BuildAgent\work\cc82e7f9f0d8d5c1\RoboContainer\Core\Container.cs:line 51

					   at PotentialCounteragentsRate.Program.Run() in c:\Projects\diadoc\_Src\Tools\PotentialCounteragentsRate\Program.cs:line 24

					   at PotentialCounteragentsRate.Program.<Main>b__0(Program p) in c:\Projects\diadoc\_Src\Tools\PotentialCounteragentsRate\Program.cs:line 17

					   at Diadoc.Protocols.Logging.ByCommandLineFactory`1.<>c__DisplayClass3.<StartService>b__2(TService p) in c:\Projects\diadoc\_Src\Logging\Diadoc.Protocols.Logging\ByCommandLineFactory.cs:line 41

					   at Diadoc.Protocols.Logging.ByCommandLineFactory`1.StartTool(IEnumerable`1 args, Func`2 runService, ILog log) in c:\Projects\diadoc\_Src\Logging\Diadoc.Protocols.Logging\ByCommandLineFactory.cs:line 65

					""" ,
"""

					Diadoc.UserService.Impl.UserSubscriptionsMigrator Diadoc.KeNotificationIndexHost Migration of subscription to user c3c4f4cc-7529-4da3-9e0c-a0b47debdd30 from 67ad8ad0-f73e-4fd6-a77c-378165bdde29;a7edb19b-0ace-4dbe-8d36-18402e720133 was skipped: 'migrated-from' users have no subscription (null)

					""" ,
"""

					Diadoc.TimeStampServer.Impl.SignatureService.SignatureService Diadoc.TimeStampServerHost Some CA certificate in the chain is not valid for the reason UntrustedRoot, RevocationStatusUnknown, OfflineRevocation. Certificate: https://diadoc.kontur.ru/Certificate/Check?base64Cert=MIIGUTCCBgCgAwIBAgIKZ…2Fq1IN5b9T0jcTo3qd27lDsz07geLxp8yyOKlUe1GvGiPCxnIWQhIXQVEmRJL6A8kZmw%3D%3D (null)

					""" ,
"""

					Diadoc.FnsClaim.Impl.Tools.ClaimLogger.ClaimLogger Diadoc.FnsClaimHost ClaimId: d0ea04ee-6202-4da2-9951-4fd97b1c8730; ImportId: d6da9d14-d6c0-46b4-b998-5ba0b33d5b55 (no context): Claim processing is failed. Error is: Diadoc.App.Common.UserFriendlyException: ErrorCode: UserFriendly.Undefined (Http.Conflict), SystemMessage: В данный момент система не позволяет отправлять документы, содержащие более 28 страниц. Это связано с приказом ФНС N ММВ-7-6/535@ и временными техническими ограничениями. За более подробной информацией вы можете обратиться в техподдержку по телефону 8 800 500-10-18, ApiClientMessage: , UserMessage: В данный момент система не позволяет отправлять документы, содержащие более 28 страниц. Это связано с приказом ФНС N ММВ-7-6/535@ и временными техническими ограничениями. За более подробной информацией вы можете обратиться в техподдержку по телефону 8 800 500-10-18 RequestId: 480eccd8-04c1-4442-b75d-570355ade2a9, Thumbprint: beb10c7966e6dc6e88e692b7c28676d5fcecaee7, ClientSystemId: diadoc.web, Locale: ru, SessionId: 00000000-0000-0000-0000-000000000000

					e8b0529a-138d-4d62-9c56-92c031b9a3da

					beb10c7966e6dc6e88e692b7c28676d5fcecaee7

					635495358616081032

					0

					9A52B0E88D13624D9C5692C031B9A3DAEDD826BBE7310D46AA7D92FC52271D17, UserId: e8b0529a-138d-4d62-9c56-92c031b9a3da, ClaimID: d0ea04ee-6202-4da2-9951-4fd97b1c8730, ImportID: d6da9d14-d6c0-46b4-b998-5ba0b33d5b55

					""" ,
"""

					Diadoc.Web.Commons.HttpApplicationBase DC.ConnectorAdmin Unhandled exception. RequestId: , Url: http://connector-admin:8082/connector-admin/GoogleGateway/BatchList (null)

					System.InvalidOperationException: Session has no diadoc token: Id: c82bf9c7-be7b-4c73-b5aa-9f2603ac9871, ExpireAt: 22.10.2014 4:36:06

					   at Diadoc.Web.Sessions.SessionExtensions.GetDiadocToken(Session session)

					   at Diadoc.Web.Sessions.SessionExtensions.GetUserId(Session session)

					   at Diadoc.Web.Sessions.UserPermissionsSessionExtensions.GetUserPermissions(Session session)

					   at DC.WebAdmin.Common.DiadocAuthorizeAttribute.AuthorizeCore(HttpContextBase httpContext)

					   at System.Web.Mvc.AuthorizeAttribute.OnAuthorization(AuthorizationContext filterContext)

					   at System.Web.Mvc.ControllerActionInvoker.InvokeAuthorizationFilters(ControllerContext controllerContext, IList`1 filters, ActionDescriptor actionDescriptor)

					   at System.Web.Mvc.ControllerActionInvoker.InvokeAction(ControllerContext controllerContext, String actionName)

					   at System.Web.Mvc.Controller.ExecuteCore()

					   at System.Web.Mvc.ControllerBase.Execute(RequestContext requestContext)

					   at System.Web.Mvc.MvcHandler.<>c__DisplayClass6.<>c__DisplayClassb.<BeginProcessRequest>b__5()

					   at System.Web.Mvc.Async.AsyncResultWrapper.<>c__DisplayClass1.<MakeVoidDelegate>b__0()

					   at System.Web.HttpApplication.CallHandlerExecutionStep.System.Web.HttpApplication.IExecutionStep.Execute()

					   at System.Web.HttpApplication.ExecuteStep(IExecutionStep step, Boolean& completedSynchronously)

					""" ,
"""

					Diadoc.Kanso Diadoc.DeliveryManHost [KansoWrite-185202680645] Shelf upload to MiniMaster 192.168.58.13:8877 failed with status ConnectionError. ShelfId = 21ef668c-385d-41a1-9be2-bfa40e3c1c54. (null)

					""" ,
"""

					Diadoc.FnsClaim.ClientImpl.Storage.Database.ClaimedDocumentDatabaseCluster diadoc.web Cannot perform request to replica: ServiceName: claim-v2, ConnectionString: Server=dd15;Database=diadoc;Uid=claim;Pwd="Bcnht,jdfybzCenmDtotq";Unicode=True;Validate Connection=True;Default Command Timeout=30;Connection Timeout=5, ReplicaType: Master, Error: ErrorCode: , ErrorMessage: Connection must be opened. (null)

					BLToolkit.Data.DataException: Connection must be opened. ---> System.InvalidOperationException: Connection must be opened.

					   at Devart.Common.Utils.CheckConnectionOpen(IDbConnection connection)

					   at Devart.Data.MySql.MySqlConnection.Rollback()

					   at Devart.Data.MySql.MySqlTransaction.Dispose(Boolean disposing)

					   at BLToolkit.Data.DbManager.ExecuteOperation(OperationType operationType, Action operation)

					   --- End of inner exception stack trace ---

					   at BLToolkit.Data.DbManager.OnOperationException(OperationType op, DataException ex)

					   at BLToolkit.Data.DbManager.HandleOperationException(OperationType op, Exception ex)

					   at BLToolkit.Data.DbManager.ExecuteOperation(OperationType operationType, Action operation)

					   at BLToolkit.Data.DbManager.Close()

					   at BLToolkit.Data.DbManager.Dispose(Boolean disposing)

					   at System.ComponentModel.Component.Dispose()

					   at DiadocSys.Net.MySql.MySql.MySqlClusterClient.TryPerformRequest(IRequestContext requestContext, Action`1 requestAction, MySqlReplica replica, ICollection`1 errors, Boolean allowRetry)

					""" ,
"""

					Diadoc.Kanso Diadoc.OvermindHost [KansoRead-176108573806] MasterLocationCache. Released updater lock by timeout (00:00:15). (null)

					""" ,
"""

					Diadoc.EventsTimeline.EventTimeline.TimelineSynchronizer Diadoc.FnsClaimHost DoPerformIteration() failed in worker lms-sync (null)

					System.TimeoutException: The task didn't complete before timeout.

					   at Cassandra.TaskHelper.WaitToComplete[T](Task`1 task, Int32 timeout) in c:\projects\diadoc\dev\external\datastax-csharp-driver\src\Cassandra\TaskHelper.cs:line 137

					   at Cassandra.Session.Execute(IStatement statement) in c:\projects\diadoc\dev\external\datastax-csharp-driver\src\Cassandra\Session.cs:line 194

					   at Diadoc.Cassandra.CassandraSession.DoExecute(CqlQuery query, Boolean executeSerial) in c:\cement\diadoc\_Src\DiadocSys\Diadoc.Cassandra\CassandraSession.cs:line 88

					   at DiadocSys.Core.PerfCounters.CallDurationsHistogram.Register[T](Func`1 action) in c:\cement\diadocsys\_Src\DiadocSys.Core\PerfCounters\CallDurationsHistogram.cs:line 33

					   at Diadoc.EventsTimeline.EventTimeline.EventTimelineMetadataStorage.GetTimelinePhases() in c:\cement\diadoc\_Src\DiadocSys\Diadoc.EventsTimeline\EventTimeline\EventTimelineMetadataStorage.cs:line 31

					   at Diadoc.EventsTimeline.EventTimeline.TimelineSynchronizer.DoPerformIteration() in c:\cement\diadoc\_Src\DiadocSys\Diadoc.EventsTimeline\EventTimeline\TimelineSynchronizer.cs:line 23

					   at DiadocSys.Threading.IterativeBackgroundThreadWorker.PerformIteration() in c:\cement\diadocsys\_Src\DiadocSys.Threading\IterativeBackgroundThreadWorker.cs:line 46

					""" ,
"""

					Diadoc.UserService.Impl.UserEmployeesMigrator Diadoc.CloudCryptHost Migration of employees to user 4fb64d06-e761-4a9b-a9fa-0665fa7e19a2 from 8b0d5acf-858f-42a7-8066-e8531c27cdcc was skipped: 'migrated-from' user has no employees (null)

					""" ,
"""

					Diadoc.Workflow.DocumentService.Patching.Torg12Patching.Torg12Patcher diadoc.web Failed to patch torg12, patchingContext: UtcNow: 10/22/2014 1:31:39 AM, Position: Оператор-бухгалтер, UserFIO:   , OrgInn: 7734695285, IsOrgIndividual: False, IndividualStateRegistrationCertificateInfo: , SenderFnsParticipantId: 2BM-7734695285-773401001-201312200939428522872, RecipientFnsParticipantId: , UserId: d049c168-0118-47c8-baed-04364494636f (null)

					System.InvalidOperationException: Неправильное имя физического лица '  '

					   at DiadocFormats.Gnivc.Patchers.XmlSignerCreator.CreateJuridicalSigner(XmlPatchingContext context)

					   at Diadoc.Workflow.DocumentService.Patching.Torg12Patching.Torg12Patcher.PatchTorg12XmlModel(Torg12SellerTitle source, XmlPatchingContext patchingContext)

					   at Diadoc.Workflow.DocumentService.Patching.Torg12Patching.Torg12Patcher.PatchSellerTitle(Byte[] source, XmlPatchingContext patchingContext)

					""" ,
"""

					Diadoc.Registration.Auto.QualifiedCertificateOrganizationRegistrator diadoc.web Qualified certificate Thumbprint: 0C1335225BB873AE7B7F727DBB0B54BDA8743344, Inn: 7812014560, OrgName: ОАО "МЕГАФОН" auto-registration skipped - found 9 different organizations with inn 7812014560 (null)

					""" ,
"""

					DDAnalyser.Program DDAnalyser Failed to start service (null)

					System.IO.FileNotFoundException: Не найден файл настроек settings/topology/statistics.

					   at Diadoc.Commons.SettingsFile`1.ReloadSettings() in f:\Projects\diadoc\_Src\Common\Diadoc.Commons\SettingsFile.cs:line 37

					   at Diadoc.Commons.SettingsFile`1.GetSettings() in f:\Projects\diadoc\_Src\Common\Diadoc.Commons\SettingsFile.cs:line 28

					   at Diadoc.Protocols.Topology.MySql.MySqlTopologySettings.GetFreshAddresses() in f:\Projects\diadoc\_Src\Transport\Diadoc.Protocols.Topology\MySql\MySqlTopologySettings.cs:line 25

					   at Diadoc.MySql.Impl.MySqlReplicaStateProvider..ctor(Func`1 getReplicas, UInt64 secondsBehindMasterLimit, Int32 checkIntervalInSeconds) in f:\Projects\diadoc\_Src\Infrastructure\Diadoc.MySql.Impl\MySqlReplicaStateProvider.cs:line 27

					   at Diadoc.MySql.Impl.MysqlClusterClient..ctor(Func`1 getReplicas, Boolean runRequestSpy) in f:\Projects\diadoc\_Src\Infrastructure\Diadoc.MySql.Impl\MysqlClusterClient.cs:line 46

					   at DDAnalyser.Program.Run() in f:\Projects\diadoc\_Src\Logging\DDAnalyser\Program.cs:line 32

					   at DDAnalyser.Program.<Main>b__0(Program p) in f:\Projects\diadoc\_Src\Logging\DDAnalyser\Program.cs:line 23

					   at Diadoc.Logs.ByCommandLineFactory`1.<>c__DisplayClass3.<StartService>b__2(TService p) in f:\Projects\diadoc\_Src\Infrastructure\Diadoc.Logs\ByCommandLineFactory.cs:line 67

					   at Diadoc.Logs.ByCommandLineFactory`1.StartTool(IEnumerable`1 args, Func`2 runService, ILog log) in f:\Projects\diadoc\_Src\Infrastructure\Diadoc.Logs\ByCommandLineFactory.cs:line 91

					""" ,
"""

					DiadocCommons.Http.Server.DiadocHttpServer Diadoc.OrganizationsDomainHost Could not process http request: Id: ce1797fc-24cf-4ee5-91e4-280065f51576, Url: http://192.168.52.68:48002/Organizations.v1/Organizations/c54bf008-fa6f-466f-80ff-b45eb713a765/SendIfnsRequest, Transcript:

					Headers:

					X-Diadoc-ClientTimeout: 10000

					X-Diadoc-Context-RequestId: ce1797fc-24cf-4ee5-91e4-280065f51576

					X-Diadoc-Context-Thumbprint: 6c453ba97e8dfd6a2f370424fcb12a9066467a23

					X-Diadoc-Context-ClientSystemId: diadoc.web

					X-Diadoc-Context-Locale: ru

					X-Diadoc-Context-SessionId: 00000000-0000-0000-0000-000000000000%0A71a6c4af-ba80-4a21-a1e3-fd6210c63db6%0A6c453ba97e8dfd6a2f370424fcb12a9066467a23%0A635495194010660508%0A0%0AAFC4A67180BA214AA1E3FD6210C63DB60B1E1DEE67DF3C4494ECCCCF17A8A204

					X-Diadoc-Context-UserId: 71a6c4af-ba80-4a21-a1e3-fd6210c63db6

					Connection: Keep-Alive

					Content-Length: 2534

					Content-Type: application/octet-stream

					Accept: application/octet-stream

					Expect: 100-continue

					Host: 192.168.52.68:48002

					Body:

					Body-Length: 2534 (null)

					Diadoc.Protocols.FnsReg.FnsRegMessageException: Organization does not have OGRN: OrgId: c54bf008-fa6f-466f-80ff-b45eb713a765, BoxId: bed9afcb-a591-4179-b53b-f4690dac02e2, FnsParticipantId: 2BM-7734670700-2013022203462437575480000000000, Inn: 7734670700, Kpp: 773401001, ShortName: ООО "Кулинар", Timestamp: Ticks: 635334173290000000, DateTime: 2014-04-18 11:28:49Z, CreationTimestamp: Ticks: 634896968420000000, DateTime: 2012-11-28 10:54:02Z, DeletedTimestamp: , BillingAccountId: b7422dfb-608d-41b5-9e03-ba45cf48112a, AbonId: , JoinedTimestamp: Ticks: 634896968420000000, DateTime: 2012-11-28 10:54:02Z, FnsRegistrationDate: , FirstActivityTimestamp: , IsBranch: False, IsPilot: False, DelegateGnivcSvcTxs: , Properties: Ogrn: , IfnsCode: , CountryCode: , ForeignAddress: , PostCode: , RegionCode: , Region: , District: , City: , Settlement: , Street: , House: , Building: , FlatOrOffice: , FirstName: , MiddleName: , LastName: , CertificateOfRegistryInfo:

					   at Diadoc.Protocols.FnsReg.FnsRegManager.GetOrgInfo(IRequestContext requestContext, Organization org) in c:\cement\diadoc\_Src\Organizations\Diadoc.Protocols.FnsReg\FnsRegManager.cs:line 142

					   at Diadoc.Protocols.FnsReg.FnsRegManager.GetFnsRegDaskForOrganization(IRequestContext requestContext, Organization org, DateTime fnsRegistrationDateIfNotSet) in c:\cement\diadoc\_Src\Organizations\Diadoc.Protocols.FnsReg\FnsRegManager.cs:line 132

					   at Diadoc.Protocols.FnsReg.FnsRegManager.SendFnsRegMessage(IRequestContext requestContext, Guid boxId, Certificate[] certificates) in c:\cement\diadoc\_Src\Organizations\Diadoc.Protocols.FnsReg\FnsRegManager.cs:line 60

					   at Diadoc.Protocols.FnsReg.IfnsService.SendFnsRegMessage(IRequestContext requestContext, Guid boxId, Certificate certificate) in c:\cement\diadoc\_Src\Organizations\Diadoc.Protocols.FnsReg\IfnsService.cs:line 40

					   at Diadoc.Organizations.Impl.Rest.RestOrganization.SendIfnsRequestImpl(SendIfnsRequestCommandArgs args) in c:\cement\diadoc\_Src\Organizations\Organizations.Impl\Rest\RestOrganization.cs:line 101

					   at Castle.DynamicProxy.AbstractInvocation.Proceed() in d:\work\16de7b8c88ab14af\src\Castle.Core\DynamicProxy\AbstractInvocation.cs:line 123

					   at Castle.DynamicProxy.AbstractInvocation.Proceed() in d:\work\16de7b8c88ab14af\src\Castle.Core\DynamicProxy\AbstractInvocation.cs:line 145

					   at Diadoc.Rest.Server.DomainAction`1.Diadoc.Rest.Server.Domain.IDomainCommandInvoker.Invoke(Object args) in c:\cement\diadoc\_Src\DiadocSys\Diadoc.Rest\Server\DomainAction.cs:line 72

					   at Diadoc.Rest.Server.Http.RestHttpHandler.ProcessCommandInvocationRequest(IHttpContext httpContext, IServerDomainNode domainNode, IRequestContext requestContext) in c:\cement\diadoc\_Src\DiadocSys\Diadoc.Rest\Server\Http\RestHttpHandler.cs:line 111

					   at Diadoc.Rest.Server.Http.RestHttpHandler.GetResponse(IHttpContext httpContext, Func`1 getResponse) in c:\cement\diadoc\_Src\DiadocSys\Diadoc.Rest\Server\Http\RestHttpHandler.cs:line 80

					   at Diadoc.Rest.Server.Http.RestHttpHandler.ProcessRequest(NameValueCollection queryString, IHttpContext httpContext) in c:\cement\diadoc\_Src\DiadocSys\Diadoc.Rest\Server\Http\RestHttpHandler.cs:line 52

					   at DiadocSys.Net.Http.Server.HttpServer.ProcessSyncRequest(IHttpContext httpContext, RequestHandlerFactory requestHandlerFactory) in c:\cement\diadocsys\_Src\DiadocSys.Net.Http\Server\HttpServer.cs:line 215

					""" ,
"""

					DiadocCommons.Rabbit.DiadocRabbitClusterClient Diadoc.FnsClaimHost Can not create channel. Attempt 1 failed. Reconnecting... (null)

					RabbitMQ.Client.Exceptions.AlreadyClosedException: Already closed: The AMQP operation was interrupted: AMQP close-reason, initiated by Library, code=541, text="Unexpected Exception", classId=0, methodId=0, cause=System.IO.IOException: Unable to read data from the transport connection: An existing connection was forcibly closed by the remote host. ---> System.Net.Sockets.SocketException: An existing connection was forcibly closed by the remote host

					   at System.Net.Sockets.NetworkStream.Read(Byte[] buffer, Int32 offset, Int32 size)

					   --- End of inner exception stack trace ---

					   at RabbitMQ.Client.Impl.Frame.ReadFrom(NetworkBinaryReader reader)

					   at RabbitMQ.Client.Impl.SocketFrameHandler_0_9.ReadFrame()

					   at RabbitMQ.Client.Impl.ConnectionBase.MainLoopIteration()

					   at RabbitMQ.Client.Impl.ConnectionBase.MainLoop()

					   at RabbitMQ.Client.Impl.SessionBase.Transmit(Command cmd)

					   at RabbitMQ.Client.Framing.Impl.v0_9_1.Model._Private_ChannelOpen(String outOfBand)

					   at RabbitMQ.Client.Impl.ConnectionBase.CreateModel()

					   at DiadocSys.Net.Rabbit.RabbitConnection.Connect() in c:\cement\diadocsys\_Src\DiadocSys.Net.Rabbit\RabbitConnection.cs:line 55

					""" ,
"""

					Diadoc.Organizations.Impl.Departments.DepartmentListItemFinder diadoc.web Not found department 9a71410b-1f13-45e0-9fd0-babc8c23c699 (null)

					""" ,
"""

					DiadocCommons.Http.Client.DiadocHttpClusterClient Diadoc.BillingHandlerHost Can't perform request: Post /Balance/ReceiveTransaction?productId=Diadoc&transactionId=b87a2ac4-e842-4fe8-b681-0f6e1aeee0b6&senderId=109422a8-8d57-4620-ae82-631bd72f20d8&recipientId=bb0f1fc9-2110-48f4-bff8-bb36915a336e&resourceId=Invoice&serviceId=exchange&count=1&createDateTicks=635495383034636232&comment=%D1%81%D1%87%D0%B5%D1%82-%D1%84%D0%B0%D0%BA%D1%82%D1%83%D1%80%D0%B0%20%E2%84%96%D0%A60505252%20%D0%BE%D1%82%2016.10.14%2C%20%D0%BE%D1%82%D0%BF%D1%80%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%3A%2022.10.14%2005%3A27%20%28%D0%9C%D0%A1%D0%9A%29%2C%20%D1%81%D1%83%D0%BC%D0%BC%D0%B0%3A%201160%2C19%2C%20%D1%81%D1%81%D1%8B%D0%BB%D0%BA%D0%B0%20%D0%BD%D0%B0%20%D0%B4%D0%BE%D0%BA%D1%83%D0%BC%D0%B5%D0%BD%D1%82%3A%20https%3A%2F%2Fdiadoc.kontur.ru%2FShowDocument%3FboxId%3D481f2052-17df-46d9-bc21-b0d8f02b6f2b%26messageId%3D3fe617a5-9341-4863-bb54-5ce3cf6e30c4%26entityId%3Db87a2ac4-e842-4fe8-b681-0f6e1aeee0b6

					Body: <null>

					Exception: DiadocSys.Net.Http.Client.HttpClientException: ResponseStatusCode: NONE

					RequestUrl: http://?//Balance/ReceiveTransaction?productId=Diadoc&transactionId=b87a2ac…1-4863-bb54-5ce3cf6e30c4%26entityId%3Db87a2ac4-e842-4fe8-b681-0f6e1aeee0b6

					Could not get response from http cluster ---> System.AggregateException: Can't perform request 'POST /Balance/ReceiveTransaction?productId=Diadoc&transactionId=b87a2ac4-e842-4fe8-b681-0f6e1aeee0b6&senderId=109422a8-8d57-4620-ae82-631bd72f20d8&recipientId=bb0f1fc9-2110-48f4-bff8-bb36915a336e&resourceId=Invoice&serviceId=exchange&count=1&createDateTicks=635495383034636232&comment=%D1%81%D1%87%D0%B5%D1%82-%D1%84%D0%B0%D0%BA%D1%82%D1%83%D1%80%D0%B0%20%E2%84%96%D0%A60505252%20%D0%BE%D1%82%2016.10.14%2C%20%D0%BE%D1%82%D0%BF%D1%80%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%3A%2022.10.14%2005%3A27%20%28%D0%9C%D0%A1%D0%9A%29%2C%20%D1%81%D1%83%D0%BC%D0%BC%D0%B0%3A%201160%2C19%2C%20%D1%81%D1%81%D1%8B%D0%BB%D0%BA%D0%B0%20%D0%BD%D0%B0%20%D0%B4%D0%BE%D0%BA%D1%83%D0%BC%D0%B5%D0%BD%D1%82%3A%20https%3A%2F%2Fdiadoc.kontur.ru%2FShowDocument%3FboxId%3D481f2052-17df-46d9-bc21-b0d8f02b6f2b%26messageId%3D3fe617a5-9341-4863-bb54-5ce3cf6e30c4%26entityId%3Db87a2ac4-e842-4fe8-b681-0f6e1aeee0b6' to cluster billing2013 ServiceName: billing2013, EndPoint: https://billy-api.kontur.ru/.

					Body: <empty> ---> DiadocSys.Net.Http.Client.ReplicaFailedException: The operation has timed out ---> System.Net.WebException: The operation has timed out

					   at System.Net.HttpWebRequest.GetResponse()

					   at DiadocSys.Net.Http.Client.HttpClient.GetResponse(HttpEndPoint endPoint, IHttpRequest request) in c:\cement\diadocsys\_Src\DiadocSys.Net.Http\Client\HttpClient.cs:line 35

					   --- End of inner exception stack trace ---

					   at DiadocSys.Net.Http.Client.HttpClient.GetResponse(HttpEndPoint endPoint, IHttpRequest request) in c:\cement\diadocsys\_Src\DiadocSys.Net.Http\Client\HttpClient.cs:line 49

					   at DiadocSys.Net.Http.Client.HttpClusterClient.TryGetResponse(IHttpRequest request, HttpReplica replica, ICollection`1 errors) in c:\cement\diadocsys\_Src\DiadocSys.Net.Http\Client\HttpClusterClient.cs:line 91

					   --- End of inner exception stack trace ---

					   --- End of inner exception stack trace ---

					   at DiadocSys.Net.Http.Client.HttpClusterClient.DoGetResponse(IHttpRequest request, Cluster`1 cluster, ICollection`1 errors, Int32 attempt, Int32 maxTryCount) in c:\cement\diadocsys\_Src\DiadocSys.Net.Http\Client\HttpClusterClient.cs:line 61

					   at DiadocSys.Net.Http.Client.HttpClusterClient.GetResponse(IHttpRequest request, Nullable`1 clientId, Nullable`1 maxTryCount) in c:\cement\diadocsys\_Src\DiadocSys.Net.Http\Client\HttpClusterClient.cs:line 44

					   at DiadocSys.Net.Http.Client.HttpClusterClientExtensions.PerformVoidHttpRequest(IHttpClusterClient httpClient, IRequestContext requestContext, String queryString, HttpMethod httpMethod, HttpRequestBody httpRequestBody, Nullable`1 clientId) in c:\cement\diadocsys\_Src\DiadocSys.Net.Http\Client\HttpClusterClientExtensions.cs:line 108 ClientSystemId: kansoTailReader, Authorization: skip, RequestId: 67cc59e8-19b6-474a-adab-f520b5d7ec11

					""" ,
"""

					DiadocSys.Tasks.TiedTasks.TiedTaskHandler Diadoc.FnsClaimHost Diadoc.App.Common.UserFriendlyException: ErrorCode: UserFriendly.Undefined (Http.Conflict), SystemMessage: В данный момент система не позволяет отправлять документы, содержащие более 28 страниц. Это связано с приказом ФНС N ММВ-7-6/535@ и временными техническими ограничениями. За более подробной информацией вы можете обратиться в техподдержку по телефону 8 800 500-10-18, ApiClientMessage: , UserMessage: В данный момент система не позволяет отправлять документы, содержащие более 28 страниц. Это связано с приказом ФНС N ММВ-7-6/535@ и временными техническими ограничениями. За более подробной информацией вы можете обратиться в техподдержку по телефону 8 800 500-10-18

					   at Diadoc.FnsClaim.Impl.Import.FileToClaim.FileToClaimPipelineFactory.BeginJpg2Rec(Guid claimId, Guid importId, FileToImgTaskResult fileImgs, IClaimLoggerFactory loggerFactory, IRecognitionStatisticsCollector statsCollector) in c:\cement\diadoc\_Src\FnsClaim\Diadoc.FnsClaim.Impl\Import\FileToClaim\FileToClaimPipelineFactory.cs:line 85

					   at Diadoc.FnsClaim.Impl.Import.FileToClaim.FileToClaimPipelineFactory.<CreatePipeline>b__3(FileToClaimPipelineItem p) in c:\cement\diadoc\_Src\FnsClaim\Diadoc.FnsClaim.Impl\Import\FileToClaim\FileToClaimPipelineFactory.cs:line 40

					   at DiadocSys.Tasks.TiedTasks.Pipeline.TiedTaskMapPipelineStep`2.Process(TiedTaskQueueItem task, TiedTaskResult[] childResults, ITiedTaskContext taskContext) in c:\cement\diadoc\_Src\DiadocSys\DiadocSys.Tasks\TiedTasks\Pipeline\TiedTaskMapPipelineStep.cs:line 33

					   at DiadocSys.Tasks.TiedTasks.TiedTaskHandler.Process(TiedTaskQueueItem task, TiedTaskResult[] childTaskResults, IRequestContext requestContext, Boolean isCancelled) in c:\cement\diadoc\_Src\DiadocSys\DiadocSys.Tasks\TiedTasks\TiedTaskHandler.cs:line 168 RequestId: 480eccd8-04c1-4442-b75d-570355ade2a9, Thumbprint: beb10c7966e6dc6e88e692b7c28676d5fcecaee7, ClientSystemId: diadoc.web, Locale: ru, SessionId: 00000000-0000-0000-0000-000000000000

					e8b0529a-138d-4d62-9c56-92c031b9a3da

					beb10c7966e6dc6e88e692b7c28676d5fcecaee7

					635495358616081032

					0

					9A52B0E88D13624D9C5692C031B9A3DAEDD826BBE7310D46AA7D92FC52271D17, UserId: e8b0529a-138d-4d62-9c56-92c031b9a3da, ClaimID: d0ea04ee-6202-4da2-9951-4fd97b1c8730, ImportID: d6da9d14-d6c0-46b4-b998-5ba0b33d5b55

					""" ,
"""

					Diadoc.Web.Commons.HttpApplicationBase diadoc.web Error to log url (null)

					System.InvalidOperationException: Could not get session from http context

					   at Diadoc.Web.Sessions.HttpContextSessionExtensions.GetSession(HttpContextBase context)

					   at DiaDoc.WebApp.Views.Shared.UserMonitor.UserMonitorHelper.LogAction(HttpContextBase httpContext, OpenUrlAction urlAction, CustomAction customAction)

					   at DiaDoc.WebApp.Views.Shared.UserMonitor.UserMonitorHelper.LogUrl(HttpContextBase httpContext)

					   at DiaDoc.WebApp.Global.Application_EndRequest()

					""" ,
"""

					Diadoc.Web.Commons.HttpApplicationBase diadoc.web Unhandled exception. RequestId: 6d3f0417-71a5-4337-af4a-766279d10d04, ClientSystemId: diadoc.web, Locale: ru, SessionId: 00000000-0000-0000-0000-000000000000

					e013da98-9900-4f7c-871b-bd05d8900921



					635495315650207999

					0

					98DA13E000997C4F871BBD05D89009215755F5289B9D6C48952CD4F442BD49DD, UserId: e013da98-9900-4f7c-871b-bd05d8900921, Url: http://diadoc.kontur.ru/api/CloudCrypt.v1/signReceipts (null)

					System.Web.HttpException (0x80004005): ResponseStatusCode: InternalServerError

					RequestUrl: http://vm-dd-ts01:15247/CloudCrypt.v1/signReceipts

					The server encountered an internal error or misconfiguration and was unable to complete your request ---> DiadocSys.Net.Http.Client.HttpClientException: ResponseStatusCode: InternalServerError

					RequestUrl: http://vm-dd-ts01:15247/CloudCrypt.v1/signReceipts

					The server encountered an internal error or misconfiguration and was unable to complete your request

					   at DiadocSys.Net.Http.Client.HttpResponseExtensions.CheckStatusCode(IHttpResponse response, HttpStatusCode[] allowedStatusCodes)

					   at Diadoc.Rest.Client.Http.RestHttpClient.SendToServer(HttpMethod method, String url, IRequestContext requestContext, Byte[] requestBody, String contentType, String acceptContentType, Nullable`1 clientId)

					   at Diadoc.Rest.Client.Http.RestHttpClient.PostToServer(String url, IRequestContext requestContext, Byte[] args, String contentType, String acceptContentType, Nullable`1 clientId)

					   at Diadoc.Web.Commons.Views.Shared.Commons.Rest.Server.ApiController.GetRestHttpResponse(IRestHttpClient restHttpClient, IRequestContext requestContext, String domainPath, Nullable`1 clientId)

					   at Diadoc.Web.Commons.Views.Shared.Commons.Rest.Server.ApiController.GetRestHttpResponse(IRestHttpClient restHttpClient, IRequestContext requestContext, String domainPath, Nullable`1 clientId)

					   at Diadoc.Web.Commons.Views.Shared.Commons.Rest.Server.ApiController.Index(String domainPath, IRequestContext requestContext)

					   at lambda_method(Closure , ControllerBase , Object[] )

					   at System.Web.Mvc.ReflectedActionDescriptor.Execute(ControllerContext controllerContext, IDictionary`2 parameters)

					   at System.Web.Mvc.ControllerActionInvoker.InvokeActionMethod(ControllerContext controllerContext, ActionDescriptor actionDescriptor, IDictionary`2 parameters)

					   at System.Web.Mvc.ControllerActionInvoker.<>c__DisplayClass15.<InvokeActionMethodWithFilters>b__12()

					   at System.Web.Mvc.ControllerActionInvoker.InvokeActionMethodFilter(IActionFilter filter, ActionExecutingContext preContext, Func`1 continuation)

					   at System.Web.Mvc.ControllerActionInvoker.InvokeActionMethodFilter(IActionFilter filter, ActionExecutingContext preContext, Func`1 continuation)

					   at System.Web.Mvc.ControllerActionInvoker.InvokeActionMethodWithFilters(ControllerContext controllerContext, IList`1 filters, ActionDescriptor actionDescriptor, IDictionary`2 parameters)

					   at System.Web.Mvc.ControllerActionInvoker.InvokeAction(ControllerContext controllerContext, String actionName)

					   at System.Web.Mvc.Controller.ExecuteCore()

					   at System.Web.Mvc.ControllerBase.Execute(RequestContext requestContext)

					   at System.Web.Mvc.MvcHandler.<>c__DisplayClass6.<>c__DisplayClassb.<BeginProcessRequest>b__5()

					   at System.Web.Mvc.Async.AsyncResultWrapper.<>c__DisplayClass1.<MakeVoidDelegate>b__0()

					   at System.Web.HttpApplication.CallHandlerExecutionStep.System.Web.HttpApplication.IExecutionStep.Execute()

					   at System.Web.HttpApplication.ExecuteStep(IExecutionStep step, Boolean& completedSynchronously)

					""" ,
"""

					DiadocCommons.Rabbit.DiadocRabbitClusterClient Diadoc.FnsClaimHost Can not create channel. Attempt 2 failed. Reconnecting... (null)

					RabbitMQ.Client.Exceptions.OperationInterruptedException: The AMQP operation was interrupted: AMQP close-reason, initiated by Library, code=0, text="End of stream", classId=0, methodId=0, cause=System.IO.EndOfStreamException: Heartbeat missing with heartbeat == 5 seconds

					   at RabbitMQ.Client.Impl.SimpleBlockingRpcContinuation.GetReply()

					   at RabbitMQ.Client.Framing.Impl.v0_9_1.Model._Private_ChannelOpen(String outOfBand)

					   at RabbitMQ.Client.Impl.ConnectionBase.CreateModel()

					   at DiadocSys.Net.Rabbit.RabbitConnection.Connect() in c:\cement\diadocsys\_Src\DiadocSys.Net.Rabbit\RabbitConnection.cs:line 55

					""" ,
"""

					Diadoc.Registration.Auto.AutoRegistrator Diadoc.CloudCryptHost Try register certificate '5AFC0FCBFF80A716CC478643993192FD9071455E'.  organization registration skipped: certificate is not qualified (null)

					""" ,
"""

					DiaDoc.WebApp.Views.Shared.BoxSelection.BoxController diadoc.web Organization 1397542b-108f-40a2-9514-ac9ffe97b748 not found for employee (user: 66df2548-f558-4930-b975-ed621c1074ef) (null)

					""" ,
"""

					DiadocSys.Tasks.TiedTasks.TiedTaskStatsService Diadoc.FnsClaimHost Error in NotifyTaskFinished, taskType: ImageToDocMeta_v3, exception: System.AggregateException: Write operation to redis cluster failed ---> System.AggregateException: Request timeout ServiceName: redis, EndPoint: 192.168.52.12:6379

					   at DiadocSys.Net.Redis.RedisClusterClient.ExecuteRequestActionTask[TResult](IRequestContext requestContext, Task`1 task, Replica replica) in c:\cement\diadocsys\_Src\DiadocSys.Net.Redis\RedisClusterClient.cs:line 163

					   --- End of inner exception stack trace ---

					   at DiadocSys.Net.Redis.RedisClusterWriteResult..ctor(List`1 results) in c:\cement\diadocsys\_Src\DiadocSys.Net.Redis\RedisClusterWriteResult.cs:line 34

					   at DiadocSys.Net.Redis.RedisClusterClient.PerformWriteRequest(IRequestContext requestContext, Func`2 requestAction) in c:\cement\diadocsys\_Src\DiadocSys.Net.Redis\RedisClusterClient.cs:line 124

					   at DiadocSys.Net.Redis.RedisClusterClient.LPush(IRequestContext requestContext, String key, Byte[] value, Nullable`1 trim) in c:\cement\diadocsys\_Src\DiadocSys.Net.Redis\RedisClusterClient.cs:line 73

					   at DiadocSys.Tasks.TiedTasks.TiedTaskStatsService.NotifyTaskFinished(IRequestContext requestContext, String taskType, Timestamp publishTimestamp, Timestamp finishedTimestamp) in c:\cement\diadoc\_Src\DiadocSys\DiadocSys.Tasks\TiedTasks\TiedTaskStatsService.cs:line 49

					---> (Inner Exception #0) System.AggregateException: Request timeout ServiceName: redis, EndPoint: 192.168.52.12:6379

					   at DiadocSys.Net.Redis.RedisClusterClient.ExecuteRequestActionTask[TResult](IRequestContext requestContext, Task`1 task, Replica replica) in c:\cement\diadocsys\_Src\DiadocSys.Net.Redis\RedisClusterClient.cs:line 163<---



					---> (Inner Exception #1) System.AggregateException: Request timeout ServiceName: redis, EndPoint: 192.168.52.13:6379

					   at DiadocSys.Net.Redis.RedisClusterClient.ExecuteRequestActionTask[TResult](IRequestContext requestContext, Task`1 task, Replica replica) in c:\cement\diadocsys\_Src\DiadocSys.Net.Redis\RedisClusterClient.cs:line 163<---



					---> (Inner Exception #2) System.AggregateException: Request timeout ServiceName: redis, EndPoint: 192.168.52.29:6379

					   at DiadocSys.Net.Redis.RedisClusterClient.ExecuteRequestActionTask[TResult](IRequestContext requestContext, Task`1 task, Replica replica) in c:\cement\diadocsys\_Src\DiadocSys.Net.Redis\RedisClusterClient.cs:line 163<---

					 RequestId: 2bc1428e-85fb-49ee-8d7c-4b3a4e08a050, Thumbprint: ce40132fba7ed16090aa4f7595745da2b6d287cf, ClientSystemId: diadoc.web, Locale: ru, SessionId: 00000000-0000-0000-0000-000000000000

					c010c48c-e0b0-48ac-b8ac-2b49ab117075

					ce40132fba7ed16090aa4f7595745da2b6d287cf

					635494844463238255

					0

					8CC410C0B0E0AC48B8AC2B49AB117075A0BB1E5762FE4947B95D5429619C49C9, UserId: c010c48c-e0b0-48ac-b8ac-2b49ab117075, ClaimID: e79f221a-dfba-452b-8267-b8fb41b5cbdb, ImportID: c77836e6-02e4-4856-8fbc-49da88d77b5f

					""" ,
"""

					DiadocSys.Tasks.TiedTasks.TiedTaskHandler Diadoc.BillingHandlerHost DiadocSys.Net.Http.Client.HttpClientException: ResponseStatusCode: NONE

					RequestUrl: http://?//Balance/ReceiveTransaction?productId=Diadoc&transactionId=b87a2ac…1-4863-bb54-5ce3cf6e30c4%26entityId%3Db87a2ac4-e842-4fe8-b681-0f6e1aeee0b6

					Could not get response from http cluster ---> System.AggregateException: Can't perform request 'POST /Balance/ReceiveTransaction?productId=Diadoc&transactionId=b87a2ac4-e842-4fe8-b681-0f6e1aeee0b6&senderId=109422a8-8d57-4620-ae82-631bd72f20d8&recipientId=bb0f1fc9-2110-48f4-bff8-bb36915a336e&resourceId=Invoice&serviceId=exchange&count=1&createDateTicks=635495383034636232&comment=%D1%81%D1%87%D0%B5%D1%82-%D1%84%D0%B0%D0%BA%D1%82%D1%83%D1%80%D0%B0%20%E2%84%96%D0%A60505252%20%D0%BE%D1%82%2016.10.14%2C%20%D0%BE%D1%82%D0%BF%D1%80%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%3A%2022.10.14%2005%3A27%20%28%D0%9C%D0%A1%D0%9A%29%2C%20%D1%81%D1%83%D0%BC%D0%BC%D0%B0%3A%201160%2C19%2C%20%D1%81%D1%81%D1%8B%D0%BB%D0%BA%D0%B0%20%D0%BD%D0%B0%20%D0%B4%D0%BE%D0%BA%D1%83%D0%BC%D0%B5%D0%BD%D1%82%3A%20https%3A%2F%2Fdiadoc.kontur.ru%2FShowDocument%3FboxId%3D481f2052-17df-46d9-bc21-b0d8f02b6f2b%26messageId%3D3fe617a5-9341-4863-bb54-5ce3cf6e30c4%26entityId%3Db87a2ac4-e842-4fe8-b681-0f6e1aeee0b6' to cluster billing2013 ServiceName: billing2013, EndPoint: https://billy-api.kontur.ru/.

					Body: <empty> ---> DiadocSys.Net.Http.Client.ReplicaFailedException: The operation has timed out ---> System.Net.WebException: The operation has timed out

					   at System.Net.HttpWebRequest.GetResponse()

					   at DiadocSys.Net.Http.Client.HttpClient.GetResponse(HttpEndPoint endPoint, IHttpRequest request) in c:\cement\diadocsys\_Src\DiadocSys.Net.Http\Client\HttpClient.cs:line 35

					   --- End of inner exception stack trace ---

					   at DiadocSys.Net.Http.Client.HttpClient.GetResponse(HttpEndPoint endPoint, IHttpRequest request) in c:\cement\diadocsys\_Src\DiadocSys.Net.Http\Client\HttpClient.cs:line 49

					   at DiadocSys.Net.Http.Client.HttpClusterClient.TryGetResponse(IHttpRequest request, HttpReplica replica, ICollection`1 errors) in c:\cement\diadocsys\_Src\DiadocSys.Net.Http\Client\HttpClusterClient.cs:line 91

					   --- End of inner exception stack trace ---

					   --- End of inner exception stack trace ---

					   at DiadocSys.Net.Http.Client.HttpClusterClient.DoGetResponse(IHttpRequest request, Cluster`1 cluster, ICollection`1 errors, Int32 attempt, Int32 maxTryCount) in c:\cement\diadocsys\_Src\DiadocSys.Net.Http\Client\HttpClusterClient.cs:line 61

					   at DiadocSys.Net.Http.Client.HttpClusterClient.GetResponse(IHttpRequest request, Nullable`1 clientId, Nullable`1 maxTryCount) in c:\cement\diadocsys\_Src\DiadocSys.Net.Http\Client\HttpClusterClient.cs:line 44

					   at DiadocSys.Net.Http.Client.HttpClusterClientExtensions.PerformVoidHttpRequest(IHttpClusterClient httpClient, IRequestContext requestContext, String queryString, HttpMethod httpMethod, HttpRequestBody httpRequestBody, Nullable`1 clientId) in c:\cement\diadocsys\_Src\DiadocSys.Net.Http\Client\HttpClusterClientExtensions.cs:line 115

					   at DiadocSys.Net.Http.Client.HttpClusterClientExtensions.PerformVoidHttpRequest(IHttpClusterClient httpClient, IRequestContext requestContext, String queryString, HttpMethod httpMethod, Nullable`1 clientId) in c:\cement\diadocsys\_Src\DiadocSys.Net.Http\Client\HttpClusterClientExtensions.cs:line 88

					   at DiadocCommons.Portal.Billing.BillingClient.RegisterTransaction(IRequestContext requestContext, Guid transactionId, Guid accountId, Guid counteragentAccountId, String resourceId, String serviceId, Int32 count, Timestamp timestamp, String description) in c:\cement\diadoccommons\_Src\DiadocCommons\Portal\Billing\BillingClient.cs:line 59

					   at Diadoc.Billing.Impl.Transactions.BillingTaskHandler.Process(BillingDocumentData task, ITiedTaskContext taskContext) in c:\cement\diadoc\_Src\Billing\Diadoc.Billing\Impl\Transactions\BillingTaskHandler.cs:line 28

					   at DiadocSys.Tasks.TiedTasks.Simple.TiedTaskSimpleProcessorBase`2.Process(TiedTaskQueueItem task, TiedTaskResult[] childResults, ITiedTaskContext taskContext) in c:\cement\diadoc\_Src\DiadocSys\DiadocSys.Tasks\TiedTasks\Simple\TiedTaskSimpleProcessorBase.cs:line 88

					   at DiadocSys.Tasks.TiedTasks.TiedTaskHandler.Process(TiedTaskQueueItem task, TiedTaskResult[] childTaskResults, IRequestContext requestContext, Boolean isCancelled) in c:\cement\diadoc\_Src\DiadocSys\DiadocSys.Tasks\TiedTasks\TiedTaskHandler.cs:line 168 ClientSystemId: kansoTailReader, Authorization: skip, RequestId: 67cc59e8-19b6-474a-adab-f520b5d7ec11

					""" ,
"""

					Diadoc.Kanso diadoc.web [KansoWrite-232000005192] AsyncUdpClient. Receive timeout. EndPoint: 192.168.52.253:53. Timeout: 00:00:00.5000000 (null)

					""" ,
"""

					DiadocCommons.Http.Client.DiadocHttpClusterClient Diadoc.FnsClaimHost Can't perform request 'GET find?inn=8620001915' to replica focus https://portal-services.kontur.ru/focus/.

					Body: <null> RequestId: c6469129-fa2e-4a44-b086-1b673f8baed9, Thumbprint: af6e6df5d04c3ecd90bf18328def72df43f4a03e, ClientSystemId: diadoc.web, Locale: ru, SessionId: 00000000-0000-0000-0000-000000000000

					c143484d-15a0-4913-b452-e88d338eb122

					af6e6df5d04c3ecd90bf18328def72df43f4a03e

					635495451494574852

					0

					4D4843C1A0151349B452E88D338EB122F46B1D1783F5FB4C96DD8FBE46E53239, UserId: c143484d-15a0-4913-b452-e88d338eb122, ClaimID: 85a2bef3-4e9f-46ef-b80b-3490c24e0a2b, ImportID: b08fd2f2-7fd5-46c4-83d6-2bd3009a3995

					DiadocSys.Net.Http.Client.ReplicaFailedException: Unable to connect to the remote server ---> System.Net.WebException: Unable to connect to the remote server ---> System.Net.Sockets.SocketException: A connection attempt failed because the connected party did not properly respond after a period of time, or established connection failed because connected host has failed to respond 46.17.203.252:443

					   at System.Net.Sockets.Socket.DoConnect(EndPoint endPointSnapshot, SocketAddress socketAddress)

					   at System.Net.ServicePoint.ConnectSocketInternal(Boolean connectFailure, Socket s4, Socket s6, Socket& socket, IPAddress& address, ConnectSocketState state, IAsyncResult asyncResult, Exception& exception)

					   --- End of inner exception stack trace ---

					   at System.Net.HttpWebRequest.GetResponse()

					   at DiadocSys.Net.Http.Client.HttpClient.GetResponse(HttpEndPoint endPoint, IHttpRequest request) in c:\cement\diadocsys\_Src\DiadocSys.Net.Http\Client\HttpClient.cs:line 35

					   --- End of inner exception stack trace ---

					   at DiadocSys.Net.Http.Client.HttpClient.GetResponse(HttpEndPoint endPoint, IHttpRequest request) in c:\cement\diadocsys\_Src\DiadocSys.Net.Http\Client\HttpClient.cs:line 49

					   at DiadocSys.Net.Http.Client.HttpClusterClient.TryGetResponse(IHttpRequest request, HttpReplica replica, ICollection`1 errors) in c:\cement\diadocsys\_Src\DiadocSys.Net.Http\Client\HttpClusterClient.cs:line 91

					""" ,
"""

					Diadoc.FnsClaim.ClientImpl.Storage.Database.CompositeClaimStorage diadoc.web Secondary storage fault: Claim with Id aed3a31d-8b0a-49e1-8086-2654d5e69be1 can not be found (null)

					""" ,
"""

					Diadoc.FnsClaim.ClientImpl.KeIntegration.KeDemandStorageApi.KeDemandStorage diadoc.web [10820001] attempt 1 failed. Error: System.Web.HttpException (0x80004005): Expected HTTP code 200, but was 500. Request: [GET] https://api.kontur.ru:443/archive.app/archive/content/6fa6f02bf981429ba21208e6b6e17690

					   at Archive.Api.Client.ClientUtilities.ThrowUnexpectedStatusException(HttpResponse httpResponse, HttpRequestMeta requestMeta, IWebRequestClient client, String expected)

					   at Archive.Api.Client.ArchiveClientBase.GetContentInternal(Uri url)

					   at Archive.Api.Client.ActionsPerformer.Perform[T](Func`1 function, Int32 attempts) (null)

					""" ,
"""

					Diadoc.TimeStampServer.Impl.CrlManagement.CrlDownloader Diadoc.TimeStampServerHost Failed to get crl from: http://certenroll.mruc.ru/mruc2013.crl (null)

					DiadocSys.Net.Http.Client.HttpClientException: ResponseStatusCode: NONE

					RequestUrl: http://certenroll.mruc.ru/mruc2013.crl

					HttpResponse content is absent.

					   at DiadocSys.Net.Http.Client.HttpResponseExtensions.GetResponseContent(IHttpResponse httpResponse) in c:\cement\diadocsys\_Src\DiadocSys.Net.Http\Client\HttpResponseExtensions.cs:line 39

					   at Diadoc.TimeStampServer.Impl.CrlManagement.CrlDownloader.TryGetCrl(IRequestContext context, String cdpUrl) in c:\cement\diadoc\_Src\App\Diadoc.TimeStampServer.Impl\CrlManagement\CrlDownloader.cs:line 46

					""" ,
"""

					DiadocSys.Net.Http.Client.HttpReplicaPingStateProvider Diadoc.OvermindHost Connection to replica ServiceName: overmindIndex, EndPoint: http://192.168.52.19:27184/ failed. DiadocSys.Net.Http.Client.ReplicaFailedException: The operation has timed out ---> System.Net.WebException: The operation has timed out

					   at System.Net.HttpWebRequest.GetResponse()

					   at DiadocSys.Net.Http.Client.HttpClient.GetResponse(HttpEndPoint endPoint, IHttpRequest request) in c:\cement\diadocsys\_Src\DiadocSys.Net.Http\Client\HttpClient.cs:line 35

					   --- End of inner exception stack trace ---

					   at DiadocSys.Net.Http.Client.HttpClient.GetResponse(HttpEndPoint endPoint, IHttpRequest request) in c:\cement\diadocsys\_Src\DiadocSys.Net.Http\Client\HttpClient.cs:line 49

					   at DiadocSys.Net.Http.Client.HttpReplicaPingStateProvider.IsFailedReplicaRecovered(HttpReplica replica) in c:\cement\diadocsys\_Src\DiadocSys.Net.Http\Client\HttpReplicaPingStateProvider.cs:line 32 (null)

					""" ,
"""

					Diadoc.Overmind.Impl.HttpHandlers.GenerateFnsXmlHandlerBase Diadoc.OvermindHost Invalid Torg12SellerTitle has been built. Validation result: IsValid: False, IsValidXml: True, ErrorMessage: Validation error: The 'Нетто' attribute is invalid - The value '-2' is invalid according to its datatype 'String' - The Pattern constraint failed.

					Validation error: The 'Нетто' attribute is invalid - The value '-4' is invalid according to its datatype 'String' - The Pattern constraint failed.

					Validation error: The 'Нетто' attribute is invalid - The value '-6' is invalid according to its datatype 'String' - The Pattern constraint failed.

					, Exception:  (null)

					""" ,
"""

					Diadoc.FnsClaim.ClientImpl.Storage.Database.CompositeClaimStorage Diadoc.FnsClaimHost Secondary storage failed with error Document 5a21368c-0478-4c94-b2a0-367f73492549 of claim 21a420ea-f7a7-4ad3-adfa-0b298daa9e9e does not exist while primary storage failed with error Cannot perform request to replica: ServiceName: claim-v2, ConnectionString: Server=dd15;Database=diadoc;Uid=claim;Pwd="Bcnht,jdfybzCenmDtotq";Unicode=True;Validate Connection=True;Default Command Timeout=30;Connection Timeout=5, ReplicaType: Master, Error: Sequence contains no matching element RequestId: 70b704c9-6767-4059-8cc2-6b93e106e6a0, Thumbprint: cf45703cb4bea28be7849ee6cd19ade6f89f14ee, ClientSystemId: diadoc.web, Locale: ru, SessionId: 00000000-0000-0000-0000-000000000000

					52ae5563-1ff1-4d36-a9b9-4a68fc42d588

					cf45703cb4bea28be7849ee6cd19ade6f89f14ee

					635495477182650017

					0

					6355AE52F11F364DA9B94A68FC42D58845E6F4524709774DAC5A55C96E0B9647, UserId: 52ae5563-1ff1-4d36-a9b9-4a68fc42d588, ClaimID: 21a420ea-f7a7-4ad3-adfa-0b298daa9e9e, ImportID: 5a21368c-0478-4c94-b2a0-367f73492549

					""" ,
"""

					Diadoc.FnsClaim.Impl.Tools.ClaimLogger.ClaimLogger Diadoc.FnsClaimHost ClaimId: 21a420ea-f7a7-4ad3-adfa-0b298daa9e9e; ImportId: 5a21368c-0478-4c94-b2a0-367f73492549 (no context): Claim processing is failed. Error is: System.InvalidOperationException: Cannot perform request to replica: ServiceName: claim-v2, ConnectionString: Server=dd15;Database=diadoc;Uid=claim;Pwd="Bcnht,jdfybzCenmDtotq";Unicode=True;Validate Connection=True;Default Command Timeout=30;Connection Timeout=5, ReplicaType: Master, Error: Sequence contains no matching element ---> System.InvalidOperationException: Sequence contains no matching element

					   at System.Linq.Enumerable.Single[TSource](IEnumerable`1 source, Func`2 predicate)

					   at Diadoc.FnsClaim.ClientImpl.Storage.Database.MysqlClaimStorageV1.MysqlClaim.GetDocument(Guid documentId) in c:\cement\diadoc\_Src\FnsClaim\Diadoc.FnsClaim.ClientImpl\Storage\Database\MysqlClaimStorageV1.cs:line 352

					   at Diadoc.FnsClaim.ClientImpl.Storage.Database.MysqlClaimStorageV1.<>c__DisplayClass1.<ReplaceDocumentImpl>b__0(MysqlClaim claim) in c:\cement\diadoc\_Src\FnsClaim\Diadoc.FnsClaim.ClientImpl\Storage\Database\MysqlClaimStorageV1.cs:line 456

					   at Diadoc.FnsClaim.ClientImpl.Storage.Database.MysqlClaimStorageV1.<>c__DisplayClass26`1.<WithClaimImpl>b__24(IDatabase db) in c:\cement\diadoc\_Src\FnsClaim\Diadoc.FnsClaim.ClientImpl\Storage\Database\MysqlClaimStorageV1.cs:line 636

					   at DiadocSys.Net.MySql.MySql.MySqlClusterClient.TryPerformRequest(IRequestContext requestContext, Action`1 requestAction, MySqlReplica replica, ICollection`1 errors, Boolean allowRetry) in c:\cement\diadocsys\_Src\DiadocSys.Net.MySql\MySql\MySqlClusterClient.cs:line 144

					   --- End of inner exception stack trace ---

					   at DiadocSys.Net.MySql.MySql.MySqlClusterClient.TryPerformRequest(IRequestContext requestContext, Action`1 requestAction, MySqlReplica replica, ICollection`1 errors, Boolean allowRetry) in c:\cement\diadocsys\_Src\DiadocSys.Net.MySql\MySql\MySqlClusterClient.cs:line 157

					   at DiadocSys.Net.MySql.MySql.MySqlClusterClient.DoPerformRequest(IRequestContext requestContext, Action`1 requestAction, Cluster`1 cluster, ICollection`1 errors, Int32 attempt, Boolean allowRetry) in c:\cement\diadocsys\_Src\DiadocSys.Net.MySql\MySql\MySqlClusterClient.cs:line 123

					   at DiadocSys.Net.MySql.DatabaseCluster.PerformNonRetryableWriteRequest(IDatabaseRequestContext context, Action`1 requestAction) in c:\cement\diadocsys\_Src\DiadocSys.Net.MySql\DatabaseCluster.cs:line 60

					   at Diadoc.FnsClaim.ClientImpl.Storage.Database.MysqlClaimStorageV1.WithClaimImpl[T](IRequestContext requestContext, Guid claimId, Func`2 claimFunc) in c:\cement\diadoc\_Src\FnsClaim\Diadoc.FnsClaim.ClientImpl\Storage\Database\MysqlClaimStorageV1.cs:line 628

					   at Diadoc.FnsClaim.ClientImpl.Storage.Database.MysqlClaimStorageV1.ReplaceDocumentImpl(IRequestContext requestContext, Guid claimId, Guid documentId, Boolean failOnMissing, Func`2 documentReplaceAction) in c:\cement\diadoc\_Src\FnsClaim\Diadoc.FnsClaim.ClientImpl\Storage\Database\MysqlClaimStorageV1.cs:line 451

					   at Diadoc.FnsClaim.ClientImpl.Storage.Database.MysqlClaimStorageV1.ReplaceDocument(IRequestContext requestContext, Guid claimId, Guid documentId, Func`2 documentReplaceAction) in c:\cement\diadoc\_Src\FnsClaim\Diadoc.FnsClaim.ClientImpl\Storage\Database\MysqlClaimStorageV1.cs:line 486

					   at Diadoc.FnsClaim.ClientImpl.Storage.Database.CompositeClaimStorage.<>c__DisplayClass1f.<ReplaceDocument>b__1e(IClaimStorage storage) in c:\cement\diadoc\_Src\FnsClaim\Diadoc.FnsClaim.ClientImpl\Storage\Database\CompositeClaimStorage.cs:line 121

					   at Diadoc.FnsClaim.ClientImpl.Storage.Database.CompositeClaimStorage.<>c__DisplayClass1.<DispatchAction>b__0(IClaimStorage storage) in c:\cement\diadoc\_Src\FnsClaim\Diadoc.FnsClaim.ClientImpl\Storage\Database\CompositeClaimStorage.cs:line 29

					   at Diadoc.FnsClaim.ClientImpl.Storage.Database.CompositeClaimStorage.DispatchAction[T](Func`2 action) in c:\cement\diadoc\_Src\FnsClaim\Diadoc.FnsClaim.ClientImpl\Storage\Database\CompositeClaimStorage.cs:line 72

					   at Diadoc.FnsClaim.Impl.Import.RecognizedPageMetaImporter.ImportPages(IRequestContext requestContext, Guid claimId, Guid toDocumentId, IEnumerable`1 pages) in c:\cement\diadoc\_Src\FnsClaim\Diadoc.FnsClaim.Impl\Import\PagesToClaim\RecognizedPageMetaImporter.cs:line 53

					   at Diadoc.FnsClaim.Impl.Import.PagesToClaim.PagesToClaimProcessor.ProcessImpl(FnsClaimPagesToClaimTask task, ITiedTaskContext taskContext) in c:\cement\diadoc\_Src\FnsClaim\Diadoc.FnsClaim.Impl\Import\PagesToClaim\PagesToClaimProcessor.cs:line 40

					   at Diadoc.FnsClaim.Impl.Import.ClaimTaskProcessorBase`2.Process(TTaskType task, ITiedTaskContext taskContext) in c:\cement\diadoc\_Src\FnsClaim\Diadoc.FnsClaim.Impl\Import\ClaimTaskProcessorBase.cs:line 41 RequestId: 70b704c9-6767-4059-8cc2-6b93e106e6a0, Thumbprint: cf45703cb4bea28be7849ee6cd19ade6f89f14ee, ClientSystemId: diadoc.web, Locale: ru, SessionId: 00000000-0000-0000-0000-000000000000

					52ae5563-1ff1-4d36-a9b9-4a68fc42d588

					cf45703cb4bea28be7849ee6cd19ade6f89f14ee

					635495477182650017

					0

					6355AE52F11F364DA9B94A68FC42D58845E6F4524709774DAC5A55C96E0B9647, UserId: 52ae5563-1ff1-4d36-a9b9-4a68fc42d588, ClaimID: 21a420ea-f7a7-4ad3-adfa-0b298daa9e9e, ImportID: 5a21368c-0478-4c94-b2a0-367f73492549

					"""]

tfidf_vectorizer = TfidfVectorizer(token_pattern=r'(?u)\b[a-zA-Z_\':,]+[\s(){}\[\]=.]', lowercase=False, use_idf=False)
tfidf_matrix = tfidf_vectorizer.fit(documents)

vectors = tfidf_matrix.transform(["""Diadoc.FilterIndex.Impl.LiveIndexReading.LiveIndexTaskReadQueueWorker Diadoc.FilterByStatusTimestampIndexHost Will retry request to LiveIndex (null)"""])

for s in cosine_similarity(tfidf_matrix.transform(documents), vectors):
    print s[0]

print tfidf_matrix.inverse_transform(vectors)
