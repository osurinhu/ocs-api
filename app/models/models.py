from ext.database import db

from typing import Optional
import datetime
import decimal

from sqlalchemy import DECIMAL, Date, DateTime, Double, ForeignKey, ForeignKeyConstraint, Index, LargeBinary, String, TIMESTAMP, Text, text
from sqlalchemy.dialects.mysql import BIGINT, DOUBLE, INTEGER, LONGBLOB, LONGTEXT, SMALLINT, TINYINT, VARCHAR
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Accesslog(db.Model):
    __tablename__ = 'accesslog'
    __table_args__ = (
        Index('HARDWARE_ID', 'HARDWARE_ID'),
        Index('USERID', 'USERID')
    )

    ID: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    HARDWARE_ID: Mapped[int] = mapped_column(INTEGER(11), nullable=False)
    USERID: Mapped[Optional[str]] = mapped_column(String(255))
    LOGDATE: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    PROCESSES: Mapped[Optional[str]] = mapped_column(Text)


class Accountinfo(db.Model):
    __tablename__ = 'accountinfo'
    __table_args__ = (
        Index('TAG', 'TAG'),
    )

    HARDWARE_ID: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    TAG: Mapped[Optional[str]] = mapped_column(String(255), server_default=text("'NA'"))


class AccountinfoConfig(db.Model):
    __tablename__ = 'accountinfo_config'

    ID: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    SHOW_ORDER: Mapped[int] = mapped_column(INTEGER(11), nullable=False)
    NAME_ACCOUNTINFO: Mapped[Optional[str]] = mapped_column(String(255))
    TYPE: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    NAME: Mapped[Optional[str]] = mapped_column(String(255))
    ID_TAB: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    COMMENT: Mapped[Optional[str]] = mapped_column(String(255))
    ACCOUNT_TYPE: Mapped[Optional[str]] = mapped_column(String(255))
    DEFAULT_VALUE: Mapped[Optional[str]] = mapped_column(String(255))


class AssetsCategories(db.Model):
    __tablename__ = 'assets_categories'

    ID: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    CATEGORY_NAME: Mapped[str] = mapped_column(String(255), nullable=False)
    CATEGORY_DESC: Mapped[str] = mapped_column(String(255), nullable=False)
    SQL_QUERY: Mapped[str] = mapped_column(Text, nullable=False)
    SQL_ARGS: Mapped[str] = mapped_column(Text, nullable=False)


class AuthAttempt(db.Model):
    __tablename__ = 'auth_attempt'

    ID: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    DATETIMEATTEMPT: Mapped[datetime.datetime] = mapped_column(DateTime, nullable=False)
    LOGIN: Mapped[Optional[str]] = mapped_column(VARCHAR(255, charset='utf8mb4', collation='utf8mb4_general_ci'))
    IP: Mapped[Optional[str]] = mapped_column(VARCHAR(255, charset='utf8mb4', collation='utf8mb4_general_ci'))
    SUCCESS: Mapped[Optional[int]] = mapped_column(INTEGER(11))


class Batteries(db.Model):
    __tablename__ = 'batteries'
    __table_args__ = (
        Index('HARDWARE_ID', 'HARDWARE_ID'),
        Index('MANUFACTURER', 'MANUFACTURER'),
        Index('NAME', 'NAME')
    )

    ID: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    HARDWARE_ID: Mapped[int] = mapped_column(INTEGER(11), nullable=False)
    LOCATION: Mapped[Optional[str]] = mapped_column(String(255))
    MANUFACTURER: Mapped[Optional[str]] = mapped_column(String(255))
    MANUFACTUREDATE: Mapped[Optional[str]] = mapped_column(String(10))
    SERIALNUMBER: Mapped[Optional[str]] = mapped_column(String(255))
    NAME: Mapped[Optional[str]] = mapped_column(String(255))
    CHEMISTRY: Mapped[Optional[str]] = mapped_column(String(20))
    DESIGNCAPACITY: Mapped[Optional[str]] = mapped_column(String(10))
    DESIGNVOLTAGE: Mapped[Optional[str]] = mapped_column(String(20))
    SBDSVERSION: Mapped[Optional[str]] = mapped_column(String(255))
    MAXERROR: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    OEMSPECIFIC: Mapped[Optional[str]] = mapped_column(String(255))


class Bios(db.Model):
    __tablename__ = 'bios'
    __table_args__ = (
        Index('ASSETTAG', 'ASSETTAG'),
        Index('SSN', 'SSN')
    )

    HARDWARE_ID: Mapped[int] = mapped_column(INTEGER(11), ForeignKey('hardware.ID'), primary_key=True)
    SMANUFACTURER: Mapped[Optional[str]] = mapped_column(String(255))
    SMODEL: Mapped[Optional[str]] = mapped_column(String(255))
    SSN: Mapped[Optional[str]] = mapped_column(String(255))
    TYPE: Mapped[Optional[str]] = mapped_column(String(255))
    BMANUFACTURER: Mapped[Optional[str]] = mapped_column(String(255))
    BVERSION: Mapped[Optional[str]] = mapped_column(String(255))
    BDATE: Mapped[Optional[str]] = mapped_column(String(255))
    ASSETTAG: Mapped[Optional[str]] = mapped_column(String(255))
    MMANUFACTURER: Mapped[Optional[str]] = mapped_column(String(255))
    MMODEL: Mapped[Optional[str]] = mapped_column(String(255))
    MSN: Mapped[Optional[str]] = mapped_column(String(255))


class BlacklistMacaddresses(db.Model):
    __tablename__ = 'blacklist_macaddresses'
    __table_args__ = (
        Index('MACADDRESS', 'MACADDRESS', unique=True),
    )

    ID: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    MACADDRESS: Mapped[str] = mapped_column(String(255), nullable=False, server_default=text("''"))


class BlacklistSerials(db.Model):
    __tablename__ = 'blacklist_serials'
    __table_args__ = (
        Index('SERIAL', 'SERIAL', unique=True),
    )

    ID: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    SERIAL: Mapped[str] = mapped_column(String(255), nullable=False, server_default=text("''"))


class BlacklistSubnet(db.Model):
    __tablename__ = 'blacklist_subnet'
    __table_args__ = (
        Index('SUBNET', 'SUBNET', 'MASK', unique=True),
    )

    ID: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    SUBNET: Mapped[str] = mapped_column(String(20), nullable=False, server_default=text("''"))
    MASK: Mapped[str] = mapped_column(String(20), nullable=False, server_default=text("''"))


class Config(db.Model):
    __tablename__ = 'config'

    NAME: Mapped[str] = mapped_column(String(50), primary_key=True)
    IVALUE: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    TVALUE: Mapped[Optional[str]] = mapped_column(String(255))
    COMMENTS: Mapped[Optional[str]] = mapped_column(Text)


class ConfigLdap(db.Model):
    __tablename__ = 'config_ldap'

    NAME: Mapped[str] = mapped_column(String(50), primary_key=True)
    IVALUE: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    TVALUE: Mapped[Optional[str]] = mapped_column(Text)
    COMMENTS: Mapped[Optional[str]] = mapped_column(Text)


class Conntrack(db.Model):
    __tablename__ = 'conntrack'

    IP: Mapped[str] = mapped_column(String(255), primary_key=True, server_default=text("''"))
    TIMESTAMP_: Mapped[datetime.datetime] = mapped_column('TIMESTAMP', TIMESTAMP, nullable=False, server_default=text('current_timestamp() ON UPDATE current_timestamp()'))


class Controllers(db.Model):
    __tablename__ = 'controllers'
    __table_args__ = (
        Index('HARDWARE_ID', 'HARDWARE_ID'),
    )

    ID: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    HARDWARE_ID: Mapped[int] = mapped_column(INTEGER(11), nullable=False)
    MANUFACTURER: Mapped[Optional[str]] = mapped_column(String(255))
    NAME: Mapped[Optional[str]] = mapped_column(String(255))
    CAPTION: Mapped[Optional[str]] = mapped_column(String(255))
    DESCRIPTION: Mapped[Optional[str]] = mapped_column(String(255))
    VERSION: Mapped[Optional[str]] = mapped_column(String(255))
    TYPE: Mapped[Optional[str]] = mapped_column(String(255))


class Cpus(db.Model):
    __tablename__ = 'cpus'
    __table_args__ = (
        Index('HARDWARE_ID', 'HARDWARE_ID'),
    )

    ID: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    HARDWARE_ID: Mapped[int] = mapped_column(INTEGER(11), ForeignKey('hardware.ID'), nullable=False)
    MANUFACTURER: Mapped[Optional[str]] = mapped_column(String(255))
    TYPE: Mapped[Optional[str]] = mapped_column(String(255))
    SERIALNUMBER: Mapped[Optional[str]] = mapped_column(String(255))
    SPEED: Mapped[Optional[str]] = mapped_column(String(255))
    CORES: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    L2CACHESIZE: Mapped[Optional[str]] = mapped_column(String(255))
    CPUARCH: Mapped[Optional[str]] = mapped_column(String(255))
    DATA_WIDTH: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    CURRENT_ADDRESS_WIDTH: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    LOGICAL_CPUS: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    VOLTAGE: Mapped[Optional[str]] = mapped_column(String(255))
    CURRENT_SPEED: Mapped[Optional[str]] = mapped_column(String(255))
    SOCKET: Mapped[Optional[str]] = mapped_column(String(255))

    hardware : Mapped['Hardware'] = relationship('Hardware')


class CveSearch(db.Model):
    __tablename__ = 'cve_search'

    ID: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    PUBLISHER_ID: Mapped[int] = mapped_column(INTEGER(11), nullable=False)
    NAME_ID: Mapped[int] = mapped_column(INTEGER(11), nullable=False)
    VERSION_ID: Mapped[int] = mapped_column(INTEGER(11), nullable=False)
    CVSS: Mapped[decimal.Decimal] = mapped_column(DOUBLE(4, 2), nullable=False)
    CVE: Mapped[Optional[str]] = mapped_column(String(255))
    LINK: Mapped[Optional[str]] = mapped_column(String(255))


class CveSearchComputer(db.Model):
    __tablename__ = 'cve_search_computer'

    ID: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    HARDWARE_ID: Mapped[int] = mapped_column(INTEGER(11), nullable=False)
    HARDWARE_NAME: Mapped[str] = mapped_column(VARCHAR(255, charset='utf8mb4', collation='utf8mb4_general_ci'), nullable=False)
    PUBLISHER: Mapped[str] = mapped_column(VARCHAR(255, charset='utf8mb4', collation='utf8mb4_general_ci'), nullable=False)
    VERSION: Mapped[str] = mapped_column(VARCHAR(255, charset='utf8mb4', collation='utf8mb4_general_ci'), nullable=False)
    SOFTWARE_NAME: Mapped[str] = mapped_column(VARCHAR(255, charset='utf8mb4', collation='utf8mb4_general_ci'), nullable=False)
    CVSS: Mapped[str] = mapped_column(VARCHAR(255, charset='utf8mb4', collation='utf8mb4_general_ci'), nullable=False)
    CVE: Mapped[str] = mapped_column(VARCHAR(255, charset='utf8mb4', collation='utf8mb4_general_ci'), nullable=False)
    LINK: Mapped[str] = mapped_column(VARCHAR(255, charset='utf8mb4', collation='utf8mb4_general_ci'), nullable=False)


class CveSearchCorrespondance(db.Model):
    __tablename__ = 'cve_search_correspondance'

    ID: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    NAME_REG: Mapped[str] = mapped_column(String(255), nullable=False)
    PUBLISH_RESULT: Mapped[Optional[str]] = mapped_column(String(255))
    NAME_RESULT: Mapped[Optional[str]] = mapped_column(String(255))


class CveSearchHistory(db.Model):
    __tablename__ = 'cve_search_history'

    ID: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    FLAG_DATE: Mapped[datetime.datetime] = mapped_column(DateTime, nullable=False)
    PUBLISHER_ID: Mapped[int] = mapped_column(INTEGER(11), nullable=False)
    CVE_NB: Mapped[Optional[int]] = mapped_column(INTEGER(11), server_default=text('0'))


class DeletedEquiv(db.Model):
    __tablename__ = 'deleted_equiv'
    __table_args__ = (
        Index('DELETED', 'DELETED'),
    )

    ID: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    DATE: Mapped[datetime.datetime] = mapped_column(TIMESTAMP, nullable=False, server_default=text('current_timestamp() ON UPDATE current_timestamp()'))
    DELETED: Mapped[str] = mapped_column(String(255), nullable=False)
    EQUIVALENT: Mapped[Optional[str]] = mapped_column(String(255))


class Deploy(db.Model):
    __tablename__ = 'deploy'

    NAME: Mapped[str] = mapped_column(String(255), primary_key=True)
    CONTENT: Mapped[bytes] = mapped_column(LONGBLOB, nullable=False)


class Devices(db.Model):
    __tablename__ = 'devices'
    __table_args__ = (
        Index('HARDWARE_ID', 'HARDWARE_ID'),
        Index('IVALUE', 'IVALUE'),
        Index('NAME', 'NAME'),
        Index('TVALUE', 'TVALUE')
    )

    ID: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    HARDWARE_ID: Mapped[int] = mapped_column(INTEGER(11), nullable=False)
    NAME: Mapped[str] = mapped_column(String(50), nullable=False)
    IVALUE: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    TVALUE: Mapped[Optional[str]] = mapped_column(String(255))
    COMMENTS: Mapped[Optional[str]] = mapped_column(Text)


class Devicetype(db.Model):
    __tablename__ = 'devicetype'

    ID: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    NAME: Mapped[Optional[str]] = mapped_column(String(255))


class DicoIgnored(db.Model):
    __tablename__ = 'dico_ignored'

    EXTRACTED: Mapped[str] = mapped_column(String(255), primary_key=True)


class DicoSoft(db.Model):
    __tablename__ = 'dico_soft'

    EXTRACTED: Mapped[str] = mapped_column(String(255), primary_key=True)
    FORMATTED: Mapped[str] = mapped_column(String(255), nullable=False)


class DownloadAffectRules(db.Model):
    __tablename__ = 'download_affect_rules'

    ID: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    RULE: Mapped[int] = mapped_column(INTEGER(11), nullable=False)
    PRIORITY: Mapped[int] = mapped_column(INTEGER(11), nullable=False)
    CFIELD: Mapped[str] = mapped_column(String(20), nullable=False)
    OP: Mapped[str] = mapped_column(String(20), nullable=False)
    COMPTO: Mapped[str] = mapped_column(String(20), nullable=False)
    RULE_NAME: Mapped[str] = mapped_column(String(200), nullable=False)
    SERV_VALUE: Mapped[Optional[str]] = mapped_column(String(20))


class DownloadAvailable(db.Model):
    __tablename__ = 'download_available'

    FILEID: Mapped[str] = mapped_column(String(255), primary_key=True)
    NAME: Mapped[str] = mapped_column(String(255), nullable=False)
    PRIORITY: Mapped[int] = mapped_column(INTEGER(11), nullable=False)
    FRAGMENTS: Mapped[int] = mapped_column(INTEGER(11), nullable=False)
    SIZE: Mapped[int] = mapped_column(INTEGER(11), nullable=False)
    OSNAME: Mapped[str] = mapped_column(String(255), nullable=False)
    COMMENT: Mapped[Optional[str]] = mapped_column(Text)
    ID_WK: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    DELETED: Mapped[Optional[int]] = mapped_column(INTEGER(11), server_default=text('0'))


class DownloadEnable(db.Model):
    __tablename__ = 'download_enable'
    __table_args__ = (
        Index('FILEID', 'FILEID'),
    )

    ID: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    FILEID: Mapped[str] = mapped_column(String(255), nullable=False)
    INFO_LOC: Mapped[str] = mapped_column(String(255), nullable=False)
    PACK_LOC: Mapped[str] = mapped_column(String(255), nullable=False)
    CERT_PATH: Mapped[Optional[str]] = mapped_column(String(255))
    CERT_FILE: Mapped[Optional[str]] = mapped_column(String(255))
    SERVER_ID: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    GROUP_ID: Mapped[Optional[int]] = mapped_column(INTEGER(11))


class DownloadHistory(db.Model):
    __tablename__ = 'download_history'

    HARDWARE_ID: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    PKG_ID: Mapped[int] = mapped_column(INTEGER(11), primary_key=True, server_default=text('0'))
    PKG_NAME: Mapped[Optional[str]] = mapped_column(String(255))


class DownloadServers(db.Model):
    __tablename__ = 'download_servers'

    HARDWARE_ID: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    URL: Mapped[str] = mapped_column(String(250), nullable=False)
    ADD_PORT: Mapped[int] = mapped_column(INTEGER(11), nullable=False)
    ADD_REP: Mapped[str] = mapped_column(String(250), nullable=False)
    GROUP_ID: Mapped[int] = mapped_column(INTEGER(11), nullable=False)


class DownloadwkConfValues(db.Model):
    __tablename__ = 'downloadwk_conf_values'

    ID: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    FIELD: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    VALUE: Mapped[Optional[str]] = mapped_column(String(100))
    DEFAULT_FIELD: Mapped[Optional[int]] = mapped_column(INTEGER(11))


class DownloadwkFields(db.Model):
    __tablename__ = 'downloadwk_fields'

    ID: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    TAB: Mapped[Optional[str]] = mapped_column(String(100))
    FIELD: Mapped[Optional[str]] = mapped_column(String(100))
    TYPE: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    LBL: Mapped[Optional[str]] = mapped_column(String(100))
    MUST_COMPLETED: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    VALUE: Mapped[Optional[str]] = mapped_column(String(255))
    DEFAULT_FIELD: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    RESTRICTED: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    LINK_STATUS: Mapped[Optional[int]] = mapped_column(INTEGER(11))


class DownloadwkHistory(db.Model):
    __tablename__ = 'downloadwk_history'

    ID: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    ID_DDE: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    AUTHOR: Mapped[Optional[str]] = mapped_column(String(255))
    DATE: Mapped[Optional[datetime.date]] = mapped_column(Date)
    ACTION: Mapped[Optional[str]] = mapped_column(LONGTEXT)


class DownloadwkPack(db.Model):
    __tablename__ = 'downloadwk_pack'

    ID: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    LOGIN_USER: Mapped[Optional[str]] = mapped_column(String(255))
    GROUP_USER: Mapped[Optional[str]] = mapped_column(String(255))
    Q_DATE: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    fields_1: Mapped[Optional[str]] = mapped_column(String(255))
    fields_2: Mapped[Optional[str]] = mapped_column(String(255))
    fields_3: Mapped[Optional[str]] = mapped_column(String(255))
    fields_4: Mapped[Optional[str]] = mapped_column(String(255))
    fields_5: Mapped[Optional[str]] = mapped_column(String(255))
    fields_6: Mapped[Optional[str]] = mapped_column(String(255))
    fields_7: Mapped[Optional[str]] = mapped_column(String(255))
    fields_8: Mapped[Optional[str]] = mapped_column(String(255))
    fields_9: Mapped[Optional[str]] = mapped_column(String(255))
    fields_10: Mapped[Optional[str]] = mapped_column(String(255))


class DownloadwkStatutRequest(db.Model):
    __tablename__ = 'downloadwk_statut_request'

    ID: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    NAME: Mapped[Optional[str]] = mapped_column(String(20))
    LBL: Mapped[Optional[str]] = mapped_column(String(255))
    ACTIF: Mapped[Optional[int]] = mapped_column(INTEGER(11))


class DownloadwkTabValues(db.Model):
    __tablename__ = 'downloadwk_tab_values'

    ID: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    FIELD: Mapped[Optional[str]] = mapped_column(String(100))
    VALUE: Mapped[Optional[str]] = mapped_column(String(100))
    LBL: Mapped[Optional[str]] = mapped_column(String(100))
    DEFAULT_FIELD: Mapped[Optional[int]] = mapped_column(INTEGER(11))


class Drives(db.Model):
    __tablename__ = 'drives'
    __table_args__ = (
        Index('HARDWARE_ID', 'HARDWARE_ID'),
    )

    ID: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    HARDWARE_ID: Mapped[int] = mapped_column(INTEGER(11), ForeignKey('hardware.ID'), nullable=False)
    LETTER: Mapped[Optional[str]] = mapped_column(String(255))
    TYPE: Mapped[Optional[str]] = mapped_column(String(255))
    FILESYSTEM: Mapped[Optional[str]] = mapped_column(String(255))
    TOTAL: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    FREE: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    NUMFILES: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    VOLUMN: Mapped[Optional[str]] = mapped_column(String(255))
    CREATEDATE: Mapped[Optional[datetime.date]] = mapped_column(Date)
    
    hardware : Mapped['Hardware'] = relationship('Hardware')


class EngineMutex(db.Model):
    __tablename__ = 'engine_mutex'
    __table_args__ = (
        Index('PID', 'PID'),
    )

    NAME: Mapped[str] = mapped_column(String(255), primary_key=True, server_default=text("''"))
    TAG: Mapped[str] = mapped_column(String(255), primary_key=True, server_default=text("''"))
    PID: Mapped[Optional[int]] = mapped_column(INTEGER(11))


class EnginePersistent(db.Model):
    __tablename__ = 'engine_persistent'
    __table_args__ = (
        Index('NAME', 'NAME', unique=True),
    )

    ID: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    NAME: Mapped[str] = mapped_column(String(255), nullable=False, server_default=text("''"))
    IVALUE: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    TVALUE: Mapped[Optional[str]] = mapped_column(String(255))


class Extensions(db.Model):
    __tablename__ = 'extensions'

    id: Mapped[str] = mapped_column(VARCHAR(255, charset='utf8mb3', collation='utf8mb3_bin'), primary_key=True)
    name: Mapped[str] = mapped_column(VARCHAR(255, charset='utf8mb3', collation='utf8mb3_bin'), nullable=False)
    version: Mapped[decimal.Decimal] = mapped_column(Double(asdecimal=True), nullable=False)
    install_date: Mapped[datetime.datetime] = mapped_column(TIMESTAMP, nullable=False, server_default=text('current_timestamp() ON UPDATE current_timestamp()'))
    description: Mapped[Optional[str]] = mapped_column(VARCHAR(255, charset='utf8mb3', collation='utf8mb3_bin'))
    licence: Mapped[Optional[str]] = mapped_column(VARCHAR(255, charset='utf8mb3', collation='utf8mb3_bin'))
    author: Mapped[Optional[str]] = mapped_column(VARCHAR(255, charset='utf8mb3', collation='utf8mb3_bin'))
    contributor: Mapped[Optional[str]] = mapped_column(VARCHAR(255, charset='utf8mb3', collation='utf8mb3_bin'))


class Files(db.Model):
    __tablename__ = 'files'

    NAME: Mapped[str] = mapped_column(String(100), primary_key=True)
    VERSION: Mapped[str] = mapped_column(String(50), primary_key=True)
    OS: Mapped[str] = mapped_column(String(70), primary_key=True)
    CONTENT: Mapped[bytes] = mapped_column(LONGBLOB, nullable=False)


class Groups(db.Model):
    __tablename__ = 'groups'

    HARDWARE_ID: Mapped[int] = mapped_column(INTEGER(11), primary_key=True, server_default=text('0'))
    REQUEST: Mapped[Optional[str]] = mapped_column(LONGTEXT)
    CREATE_TIME: Mapped[Optional[int]] = mapped_column(INTEGER(11), server_default=text('0'))
    REVALIDATE_FROM: Mapped[Optional[int]] = mapped_column(INTEGER(11), server_default=text('0'))
    XMLDEF: Mapped[Optional[str]] = mapped_column(LONGTEXT)


class GroupsCache(db.Model):
    __tablename__ = 'groups_cache'

    HARDWARE_ID: Mapped[int] = mapped_column(INTEGER(11), primary_key=True, server_default=text('0'))
    GROUP_ID: Mapped[int] = mapped_column(INTEGER(11), primary_key=True, server_default=text('0'))
    STATIC: Mapped[Optional[int]] = mapped_column(INTEGER(11), server_default=text('0'))


class Hardware(db.Model):
    __tablename__ = 'hardware'
    __table_args__ = (
        Index('CHECKSUM', 'CHECKSUM'),
        Index('DEVICEID', 'DEVICEID'),
        Index('MEMORY', 'MEMORY'),
        Index('NAME', 'NAME'),
        Index('OSNAME', 'OSNAME'),
        Index('USERID', 'USERID'),
        Index('WORKGROUP', 'WORKGROUP')
    )

    ID: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    DEVICEID: Mapped[str] = mapped_column(String(255), nullable=False)
    NAME: Mapped[Optional[str]] = mapped_column(String(255))
    WORKGROUP: Mapped[Optional[str]] = mapped_column(String(255))
    USERDOMAIN: Mapped[Optional[str]] = mapped_column(String(255))
    OSNAME: Mapped[Optional[str]] = mapped_column(String(255))
    OSVERSION: Mapped[Optional[str]] = mapped_column(String(255))
    OSCOMMENTS: Mapped[Optional[str]] = mapped_column(String(255))
    PROCESSORT: Mapped[Optional[str]] = mapped_column(String(255))
    PROCESSORS: Mapped[Optional[int]] = mapped_column(INTEGER(11), server_default=text('0'))
    PROCESSORN: Mapped[Optional[int]] = mapped_column(SMALLINT(6))
    MEMORY: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    SWAP: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    IPADDR: Mapped[Optional[str]] = mapped_column(String(255))
    DNS: Mapped[Optional[str]] = mapped_column(String(255))
    DEFAULTGATEWAY: Mapped[Optional[str]] = mapped_column(String(255))
    ETIME: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    LASTDATE: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    LASTCOME: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    QUALITY: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(7, 4))
    FIDELITY: Mapped[Optional[int]] = mapped_column(BIGINT(20), server_default=text('1'))
    USERID: Mapped[Optional[str]] = mapped_column(String(255))
    TYPE: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    DESCRIPTION: Mapped[Optional[str]] = mapped_column(String(255))
    WINCOMPANY: Mapped[Optional[str]] = mapped_column(String(255))
    WINOWNER: Mapped[Optional[str]] = mapped_column(String(255))
    WINPRODID: Mapped[Optional[str]] = mapped_column(String(255))
    WINPRODKEY: Mapped[Optional[str]] = mapped_column(String(255))
    USERAGENT: Mapped[Optional[str]] = mapped_column(String(50))
    CHECKSUM: Mapped[Optional[int]] = mapped_column(BIGINT(20, unsigned=True), server_default=text('262143'))
    SSTATE: Mapped[Optional[int]] = mapped_column(INTEGER(11), server_default=text('0'))
    IPSRC: Mapped[Optional[str]] = mapped_column(String(255))
    UUID: Mapped[Optional[str]] = mapped_column(String(255))
    ARCH: Mapped[Optional[str]] = mapped_column(String(10))
    CATEGORY_ID: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    ARCHIVE: Mapped[Optional[int]] = mapped_column(INTEGER(11))

    archive: Mapped[list['Archive']] = relationship('Archive')
    bios : Mapped[Optional['Bios']] = relationship('Bios')

class HardwareOsnameCache(db.Model):
    __tablename__ = 'hardware_osname_cache'
    __table_args__ = (
        Index('OSNAME', 'OSNAME', unique=True),
    )

    ID: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    OSNAME: Mapped[Optional[str]] = mapped_column(String(255))


class History(db.Model):
    __tablename__ = 'history'

    ID: Mapped[int] = mapped_column(BIGINT(20), primary_key=True)
    USER: Mapped[str] = mapped_column(String(255), nullable=False)
    DATETIME_ACTION: Mapped[datetime.datetime] = mapped_column(DateTime, nullable=False)
    ACTION: Mapped[str] = mapped_column(String(255), nullable=False)
    TARGET: Mapped[str] = mapped_column(String(255), nullable=False)


class Inputs(db.Model):
    __tablename__ = 'inputs'
    __table_args__ = (
        Index('HARDWARE_ID', 'HARDWARE_ID'),
    )

    ID: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    HARDWARE_ID: Mapped[int] = mapped_column(INTEGER(11), ForeignKey('hardware.ID'), nullable=False)
    TYPE: Mapped[Optional[str]] = mapped_column(String(255))
    MANUFACTURER: Mapped[Optional[str]] = mapped_column(String(255))
    CAPTION: Mapped[Optional[str]] = mapped_column(String(255))
    DESCRIPTION: Mapped[Optional[str]] = mapped_column(String(255))
    INTERFACE: Mapped[Optional[str]] = mapped_column(String(255))
    POINTTYPE: Mapped[Optional[str]] = mapped_column(String(255))
    
    hardware : Mapped['Hardware'] = relationship('Hardware')

class ItmgmtComments(db.Model):
    __tablename__ = 'itmgmt_comments'
    __table_args__ = (
        Index('HARDWARE_ID', 'HARDWARE_ID'),
    )

    ID: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    HARDWARE_ID: Mapped[int] = mapped_column(INTEGER(11), nullable=False)
    COMMENTS: Mapped[Optional[str]] = mapped_column(LONGTEXT)
    USER_INSERT: Mapped[Optional[str]] = mapped_column(String(100))
    DATE_INSERT: Mapped[Optional[datetime.date]] = mapped_column(Date)
    ACTION: Mapped[Optional[str]] = mapped_column(String(255))
    VISIBLE: Mapped[Optional[int]] = mapped_column(INTEGER(11))


class Javainfo(db.Model):
    __tablename__ = 'javainfo'

    HARDWARE_ID: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    JAVANAME: Mapped[Optional[str]] = mapped_column(String(255), server_default=text("'NONAME'"))
    JAVAPATHLEVEL: Mapped[Optional[int]] = mapped_column(INTEGER(11), server_default=text('0'))
    JAVACOUNTRY: Mapped[Optional[str]] = mapped_column(String(255))
    JAVACLASSPATH: Mapped[Optional[str]] = mapped_column(String(255))
    JAVAHOME: Mapped[Optional[str]] = mapped_column(String(255))


class Journallog(db.Model):
    __tablename__ = 'journallog'
    __table_args__ = (
        Index('HARDWARE_ID', 'HARDWARE_ID'),
    )

    HARDWARE_ID: Mapped[int] = mapped_column(INTEGER(11), nullable=False)
    ID: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    JOURNALLOG: Mapped[Optional[str]] = mapped_column(LONGTEXT)
    LISTENERNAME: Mapped[Optional[str]] = mapped_column(String(255), server_default=text("'NONAME'"))
    DATE: Mapped[Optional[str]] = mapped_column(String(255))
    STATUS: Mapped[Optional[int]] = mapped_column(INTEGER(11), server_default=text('0'))
    ERRORCODE: Mapped[Optional[int]] = mapped_column(INTEGER(11), server_default=text('0'))


class Languages(db.Model):
    __tablename__ = 'languages'

    NAME: Mapped[str] = mapped_column(String(60), primary_key=True)
    IMG: Mapped[Optional[bytes]] = mapped_column(LargeBinary)
    JSON_VALUE: Mapped[Optional[str]] = mapped_column(LONGTEXT)


class Layouts(db.Model):
    __tablename__ = 'layouts'

    ID: Mapped[int] = mapped_column(BIGINT(20), primary_key=True)
    LAYOUT_NAME: Mapped[str] = mapped_column(String(255), nullable=False)
    CREATOR: Mapped[str] = mapped_column(String(255), nullable=False)
    TABLE_NAME: Mapped[str] = mapped_column(String(255), nullable=False)
    VISIBLE_COL: Mapped[str] = mapped_column(Text, nullable=False)
    DESCRIPTION: Mapped[Optional[str]] = mapped_column(String(255))
    VISIBILITY_SCOPE: Mapped[Optional[str]] = mapped_column(String(255), server_default=text("'USER'"))
    GROUP_ID: Mapped[Optional[str]] = mapped_column(String(255))


class LocalGroups(db.Model):
    __tablename__ = 'local_groups'

    ID: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    HARDWARE_ID: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    ID_GROUP: Mapped[Optional[str]] = mapped_column(VARCHAR(255, charset='utf8mb4', collation='utf8mb4_general_ci'))
    NAME: Mapped[Optional[str]] = mapped_column(VARCHAR(255, charset='utf8mb4', collation='utf8mb4_general_ci'))
    MEMBER: Mapped[Optional[str]] = mapped_column(VARCHAR(255, charset='utf8mb4', collation='utf8mb4_general_ci'))


class LocalUsers(db.Model):
    __tablename__ = 'local_users'

    ID: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    HARDWARE_ID: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    ID_USER: Mapped[Optional[str]] = mapped_column(VARCHAR(255, charset='utf8mb4', collation='utf8mb4_general_ci'))
    GID: Mapped[Optional[str]] = mapped_column(VARCHAR(255, charset='utf8mb4', collation='utf8mb4_general_ci'))
    NAME: Mapped[Optional[str]] = mapped_column(VARCHAR(255, charset='utf8mb4', collation='utf8mb4_general_ci'))
    HOME: Mapped[Optional[str]] = mapped_column(VARCHAR(255, charset='utf8mb4', collation='utf8mb4_general_ci'))
    SHELL: Mapped[Optional[str]] = mapped_column(VARCHAR(255, charset='utf8mb4', collation='utf8mb4_general_ci'))
    LOGIN: Mapped[Optional[str]] = mapped_column(VARCHAR(255, charset='utf8mb4', collation='utf8mb4_general_ci'))
    MEMBER: Mapped[Optional[str]] = mapped_column(VARCHAR(255, charset='utf8mb4', collation='utf8mb4_general_ci'))


class Locks(db.Model):
    __tablename__ = 'locks'
    __table_args__ = (
        Index('SINCE', 'SINCE'),
    )

    HARDWARE_ID: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    SINCE: Mapped[datetime.datetime] = mapped_column(TIMESTAMP, nullable=False, server_default=text('current_timestamp() ON UPDATE current_timestamp()'))
    ID: Mapped[Optional[int]] = mapped_column(INTEGER(11))


class Memories(db.Model):
    __tablename__ = 'memories'
    __table_args__ = (
        Index('HARDWARE_ID', 'HARDWARE_ID'),
    )

    ID: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    HARDWARE_ID: Mapped[int] = mapped_column(INTEGER(11), nullable=False)
    CAPTION: Mapped[Optional[str]] = mapped_column(String(255))
    DESCRIPTION: Mapped[Optional[str]] = mapped_column(String(255))
    CAPACITY: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    PURPOSE: Mapped[Optional[str]] = mapped_column(String(255))
    TYPE: Mapped[Optional[str]] = mapped_column(String(255))
    SPEED: Mapped[Optional[str]] = mapped_column(String(255))
    NUMSLOTS: Mapped[Optional[int]] = mapped_column(SMALLINT(6))
    SERIALNUMBER: Mapped[Optional[str]] = mapped_column(String(255))


class Modems(db.Model):
    __tablename__ = 'modems'
    __table_args__ = (
        Index('HARDWARE_ID', 'HARDWARE_ID'),
    )

    ID: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    HARDWARE_ID: Mapped[int] = mapped_column(INTEGER(11), nullable=False)
    NAME: Mapped[Optional[str]] = mapped_column(String(255))
    MODEL: Mapped[Optional[str]] = mapped_column(String(255))
    DESCRIPTION: Mapped[Optional[str]] = mapped_column(String(255))
    TYPE: Mapped[Optional[str]] = mapped_column(String(255))


class Monitors(db.Model):
    __tablename__ = 'monitors'
    __table_args__ = (
        Index('HARDWARE_ID', 'HARDWARE_ID'),
    )

    ID: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    HARDWARE_ID: Mapped[int] = mapped_column(INTEGER(11), ForeignKey('hardware.ID'), nullable=False)
    MANUFACTURER: Mapped[Optional[str]] = mapped_column(String(255))
    CAPTION: Mapped[Optional[str]] = mapped_column(String(255))
    DESCRIPTION: Mapped[Optional[str]] = mapped_column(String(255))
    TYPE: Mapped[Optional[str]] = mapped_column(String(255))
    SERIAL: Mapped[Optional[str]] = mapped_column(String(255))

    hardware : Mapped['Hardware'] = relationship('Hardware')


class Netmap(db.Model):
    __tablename__ = 'netmap'
    __table_args__ = (
        Index('IP', 'IP'),
        Index('NETID', 'NETID')
    )

    IP: Mapped[str] = mapped_column(String(15), nullable=False)
    MAC: Mapped[str] = mapped_column(String(17), primary_key=True)
    MASK: Mapped[str] = mapped_column(String(15), nullable=False)
    NETID: Mapped[str] = mapped_column(String(15), nullable=False)
    DATE: Mapped[datetime.datetime] = mapped_column(TIMESTAMP, nullable=False, server_default=text('current_timestamp()'))
    NAME: Mapped[Optional[str]] = mapped_column(String(255))
    TAG: Mapped[Optional[str]] = mapped_column(String(255))
    HARDWARE_ID: Mapped[Optional[int]] = mapped_column(INTEGER(11))


class NetworkDevices(db.Model):
    __tablename__ = 'network_devices'
    __table_args__ = (
        Index('MACADDR', 'MACADDR'),
    )

    ID: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    DESCRIPTION: Mapped[Optional[str]] = mapped_column(String(255))
    TYPE: Mapped[Optional[str]] = mapped_column(String(255))
    MACADDR: Mapped[Optional[str]] = mapped_column(String(255))
    USER: Mapped[Optional[str]] = mapped_column(String(255))


class Networks(db.Model):
    __tablename__ = 'networks'
    __table_args__ = (
        Index('HARDWARE_ID', 'HARDWARE_ID'),
        Index('IPADDRESS', 'IPADDRESS'),
        Index('IPGATEWAY', 'IPGATEWAY'),
        Index('IPSUBNET', 'IPSUBNET'),
        Index('MACADDR', 'MACADDR')
    )

    ID: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    HARDWARE_ID: Mapped[int] = mapped_column(INTEGER(11), ForeignKey('hardware.ID'), nullable=False)
    DESCRIPTION: Mapped[Optional[str]] = mapped_column(String(255))
    TYPE: Mapped[Optional[str]] = mapped_column(String(255))
    TYPEMIB: Mapped[Optional[str]] = mapped_column(String(255))
    SPEED: Mapped[Optional[str]] = mapped_column(String(255))
    MTU: Mapped[Optional[str]] = mapped_column(String(255))
    MACADDR: Mapped[Optional[str]] = mapped_column(String(255))
    STATUS: Mapped[Optional[str]] = mapped_column(String(255))
    IPADDRESS: Mapped[Optional[str]] = mapped_column(String(255))
    IPMASK: Mapped[Optional[str]] = mapped_column(String(255))
    IPGATEWAY: Mapped[Optional[str]] = mapped_column(String(255))
    IPSUBNET: Mapped[Optional[str]] = mapped_column(String(255))
    IPDHCP: Mapped[Optional[str]] = mapped_column(String(255))
    VIRTUALDEV: Mapped[Optional[int]] = mapped_column(TINYINT(1), server_default=text('0'))

    hardware : Mapped['Hardware'] = relationship('Hardware')


class Notification(db.Model):
    __tablename__ = 'notification'

    ID: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    TYPE: Mapped[str] = mapped_column(String(255), nullable=False)
    FILE: Mapped[Optional[str]] = mapped_column(String(255))
    SUBJECT: Mapped[Optional[str]] = mapped_column(String(255))
    ALTBODY: Mapped[Optional[str]] = mapped_column(Text)


class NotificationConfig(db.Model):
    __tablename__ = 'notification_config'

    ID: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    NAME: Mapped[str] = mapped_column(String(255), nullable=False)
    TVALUE: Mapped[Optional[str]] = mapped_column(String(255))


class Operators(db.Model):
    __tablename__ = 'operators'

    ID: Mapped[str] = mapped_column(String(255), primary_key=True, server_default=text("''"))
    FIRSTNAME: Mapped[Optional[str]] = mapped_column(String(255))
    LASTNAME: Mapped[Optional[str]] = mapped_column(String(255))
    PASSWD: Mapped[Optional[str]] = mapped_column(String(255))
    ACCESSLVL: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    COMMENTS: Mapped[Optional[str]] = mapped_column(Text)
    NEW_ACCESSLVL: Mapped[Optional[str]] = mapped_column(String(255))
    EMAIL: Mapped[Optional[str]] = mapped_column(String(255))
    USER_GROUP: Mapped[Optional[str]] = mapped_column(String(255))
    PASSWORD_VERSION: Mapped[Optional[int]] = mapped_column(INTEGER(11), server_default=text('0'))


class Ports(db.Model):
    __tablename__ = 'ports'
    __table_args__ = (
        Index('HARDWARE_ID', 'HARDWARE_ID'),
    )

    ID: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    HARDWARE_ID: Mapped[int] = mapped_column(INTEGER(11), nullable=False)
    TYPE: Mapped[Optional[str]] = mapped_column(String(255))
    NAME: Mapped[Optional[str]] = mapped_column(String(255))
    CAPTION: Mapped[Optional[str]] = mapped_column(String(255))
    DESCRIPTION: Mapped[Optional[str]] = mapped_column(String(255))


class Printers(db.Model):
    __tablename__ = 'printers'
    __table_args__ = (
        Index('HARDWARE_ID', 'HARDWARE_ID'),
    )

    ID: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    HARDWARE_ID: Mapped[int] = mapped_column(INTEGER(11), nullable=False)
    NAME: Mapped[Optional[str]] = mapped_column(String(255))
    DRIVER: Mapped[Optional[str]] = mapped_column(String(255))
    PORT: Mapped[Optional[str]] = mapped_column(String(255))
    DESCRIPTION: Mapped[Optional[str]] = mapped_column(String(255))
    SERVERNAME: Mapped[Optional[str]] = mapped_column(String(255))
    SHARENAME: Mapped[Optional[str]] = mapped_column(String(255))
    RESOLUTION: Mapped[Optional[str]] = mapped_column(String(50))
    COMMENT: Mapped[Optional[str]] = mapped_column(String(255))
    SHARED: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    NETWORK: Mapped[Optional[int]] = mapped_column(INTEGER(11))


class PrologConntrack(db.Model):
    __tablename__ = 'prolog_conntrack'
    __table_args__ = (
        Index('DEVICEID', 'DEVICEID'),
    )

    ID: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    DEVICEID: Mapped[Optional[str]] = mapped_column(String(255))
    TIMESTAMP_: Mapped[Optional[int]] = mapped_column('TIMESTAMP', INTEGER(11))
    PID: Mapped[Optional[int]] = mapped_column(INTEGER(11))


class Regconfig(db.Model):
    __tablename__ = 'regconfig'
    __table_args__ = (
        Index('NAME', 'NAME'),
    )

    ID: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    NAME: Mapped[Optional[str]] = mapped_column(String(255))
    REGTREE: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    REGKEY: Mapped[Optional[str]] = mapped_column(Text)
    REGVALUE: Mapped[Optional[str]] = mapped_column(String(255))


class Registry(db.Model):
    __tablename__ = 'registry'
    __table_args__ = (
        Index('HARDWARE_ID', 'HARDWARE_ID'),
        Index('NAME', 'NAME')
    )

    ID: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    HARDWARE_ID: Mapped[int] = mapped_column(INTEGER(11), nullable=False)
    NAME: Mapped[Optional[str]] = mapped_column(String(255))
    REGVALUE: Mapped[Optional[str]] = mapped_column(Text)


class RegistryNameCache(db.Model):
    __tablename__ = 'registry_name_cache'
    __table_args__ = (
        Index('NAME', 'NAME', unique=True),
    )

    ID: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    NAME: Mapped[Optional[str]] = mapped_column(String(255))


class RegistryRegvalueCache(db.Model):
    __tablename__ = 'registry_regvalue_cache'

    ID: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    REGVALUE: Mapped[Optional[str]] = mapped_column(Text)


class ReportsNotifications(db.Model):
    __tablename__ = 'reports_notifications'

    ID: Mapped[int] = mapped_column(BIGINT(20), primary_key=True)
    GROUP_ID: Mapped[int] = mapped_column(INTEGER(11), nullable=False)
    RECURRENCE: Mapped[str] = mapped_column(String(255), nullable=False)
    MAIL: Mapped[str] = mapped_column(String(255), nullable=False)
    STATUS: Mapped[str] = mapped_column(String(255), nullable=False)
    END_DATE: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    DATE_CREATED: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    WEEKDAY: Mapped[Optional[str]] = mapped_column(String(255))
    LAST_EXEC: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)


class Repository(db.Model):
    __tablename__ = 'repository'
    __table_args__ = (
        Index('HARDWARE_ID', 'HARDWARE_ID'),
    )

    ID: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    HARDWARE_ID: Mapped[int] = mapped_column(INTEGER(11), nullable=False)
    BASEURL: Mapped[Optional[str]] = mapped_column(String(255))
    EXCLUDE: Mapped[Optional[str]] = mapped_column(String(255))
    EXCLUDED: Mapped[Optional[str]] = mapped_column(String(255))
    EXPIRE: Mapped[Optional[str]] = mapped_column(String(255))
    FILENAME: Mapped[Optional[str]] = mapped_column(String(255))
    MIRRORS: Mapped[Optional[str]] = mapped_column(String(255))
    NAME: Mapped[Optional[str]] = mapped_column(String(255))
    PKGS: Mapped[Optional[str]] = mapped_column(String(255))
    REVISION: Mapped[Optional[str]] = mapped_column(String(255))
    SIZE: Mapped[Optional[str]] = mapped_column(String(255))
    TAG: Mapped[Optional[str]] = mapped_column(String(255))
    UPDATED: Mapped[Optional[str]] = mapped_column(String(255))


class Saas(db.Model):
    __tablename__ = 'saas'

    ID: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    SAAS_EXP_ID: Mapped[int] = mapped_column(INTEGER(11), nullable=False)
    HARDWARE_ID: Mapped[int] = mapped_column(INTEGER(11), nullable=False)
    ENTRY: Mapped[str] = mapped_column(String(255), nullable=False)
    DATA: Mapped[str] = mapped_column(String(255), nullable=False)
    TTL: Mapped[int] = mapped_column(INTEGER(11), nullable=False)


class SaasExp(db.Model):
    __tablename__ = 'saas_exp'

    ID: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    NAME: Mapped[str] = mapped_column(String(255), nullable=False)
    DNS_EXP: Mapped[str] = mapped_column(String(255), nullable=False)


class SaveQuery(db.Model):
    __tablename__ = 'save_query'

    ID: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    QUERY_NAME: Mapped[str] = mapped_column(String(255), nullable=False)
    PARAMETERS: Mapped[str] = mapped_column(Text, nullable=False)
    DESCRIPTION: Mapped[Optional[str]] = mapped_column(Text)
    WHO_CAN_SEE: Mapped[Optional[str]] = mapped_column(String(255), server_default=text("'ALL'"))
    USER_ID: Mapped[Optional[str]] = mapped_column(String(255))
    GROUP_ID: Mapped[Optional[str]] = mapped_column(String(255))


class ScheduleWol(db.Model):
    __tablename__ = 'schedule_wol'

    ID: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    MACHINE_ID: Mapped[str] = mapped_column(String(255), nullable=False)
    WOL_DATE: Mapped[datetime.datetime] = mapped_column(DateTime, nullable=False)


class Sim(db.Model):
    __tablename__ = 'sim'
    __table_args__ = (
        Index('HARDWARE_ID', 'HARDWARE_ID'),
    )

    ID: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    HARDWARE_ID: Mapped[int] = mapped_column(INTEGER(11), nullable=False)
    OPERATOR: Mapped[Optional[str]] = mapped_column(String(255))
    OPNAME: Mapped[Optional[str]] = mapped_column(String(255))
    COUNTRY: Mapped[Optional[str]] = mapped_column(String(255))
    SERIALNUMBER: Mapped[Optional[str]] = mapped_column(String(255))
    DEVICEID: Mapped[Optional[str]] = mapped_column(String(255))
    PHONENUMBER: Mapped[Optional[str]] = mapped_column(String(255))


class Slots(db.Model):
    __tablename__ = 'slots'
    __table_args__ = (
        Index('HARDWARE_ID', 'HARDWARE_ID'),
    )

    ID: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    HARDWARE_ID: Mapped[int] = mapped_column(INTEGER(11), nullable=False)
    NAME: Mapped[Optional[str]] = mapped_column(String(255))
    DESCRIPTION: Mapped[Optional[str]] = mapped_column(String(255))
    DESIGNATION: Mapped[Optional[str]] = mapped_column(String(255))
    PURPOSE: Mapped[Optional[str]] = mapped_column(String(255))
    STATUS: Mapped[Optional[str]] = mapped_column(String(255))
    PSHARE: Mapped[Optional[int]] = mapped_column(TINYINT(4))


class SmartHealth(db.Model):
    __tablename__ = 'smart_health'

    id: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    hostname: Mapped[Optional[str]] = mapped_column(String(100))
    disco: Mapped[Optional[str]] = mapped_column(String(50))
    temperatura: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    spare_available: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    percentage_used: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    unsafe_shutdowns: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    erros: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    status: Mapped[Optional[str]] = mapped_column(String(20))
    coletado_em: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)


class SnmpAccountinfo(db.Model):
    __tablename__ = 'snmp_accountinfo'
    __table_args__ = (
        Index('TAG', 'TAG'),
    )

    ID: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    SNMP_TYPE: Mapped[str] = mapped_column(String(255), nullable=False)
    SNMP_RECONCILIATION_FIELD: Mapped[str] = mapped_column(String(255), nullable=False)
    SNMP_RECONCILIATION_VALUE: Mapped[str] = mapped_column(String(255), nullable=False)
    TAG: Mapped[Optional[str]] = mapped_column(String(255), server_default=text("'NA'"))


class SnmpCommunities(db.Model):
    __tablename__ = 'snmp_communities'

    ID: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    VERSION: Mapped[Optional[str]] = mapped_column(String(5))
    NAME: Mapped[Optional[str]] = mapped_column(String(255))
    USERNAME: Mapped[Optional[str]] = mapped_column(String(255))
    AUTHPASSWD: Mapped[Optional[str]] = mapped_column(String(255))
    AUTHPROTO: Mapped[Optional[str]] = mapped_column(String(255))
    PRIVPROTO: Mapped[Optional[str]] = mapped_column(String(255))
    PRIVPASSWD: Mapped[Optional[str]] = mapped_column(String(255))
    LEVEL: Mapped[Optional[str]] = mapped_column(String(255))


class SnmpConfigs(db.Model):
    __tablename__ = 'snmp_configs'

    ID: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    TYPE_ID: Mapped[int] = mapped_column(INTEGER(11), nullable=False)
    LABEL_ID: Mapped[int] = mapped_column(INTEGER(11), nullable=False)
    OID: Mapped[str] = mapped_column(String(255), nullable=False)
    RECONCILIATION: Mapped[Optional[str]] = mapped_column(String(255))
    IPD_RECONCILIATION: Mapped[Optional[str]] = mapped_column(String(255))


class SnmpDefault(db.Model):
    __tablename__ = 'snmp_default'
    __table_args__ = (
        Index('DefaultName', 'DefaultName', unique=True),
    )

    ID: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    DefaultName: Mapped[Optional[str]] = mapped_column(String(255))
    DefaultDescription: Mapped[Optional[str]] = mapped_column(String(255))
    DefaultLocation: Mapped[Optional[str]] = mapped_column(String(255))
    DefaultUptime: Mapped[Optional[str]] = mapped_column(String(255))
    DefaultAddressIP: Mapped[Optional[str]] = mapped_column(String(255))
    DefaultGateway: Mapped[Optional[str]] = mapped_column(String(255))


class SnmpLabels(db.Model):
    __tablename__ = 'snmp_labels'

    ID: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    LABEL_NAME: Mapped[str] = mapped_column(String(255), nullable=False)


class SnmpMibs(db.Model):
    __tablename__ = 'snmp_mibs'

    ID: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    VENDOR: Mapped[Optional[str]] = mapped_column(String(255))
    URL: Mapped[Optional[str]] = mapped_column(String(255))
    CHECKSUM: Mapped[Optional[str]] = mapped_column(String(255))
    VERSION: Mapped[Optional[str]] = mapped_column(String(5))
    PARSER: Mapped[Optional[str]] = mapped_column(String(5))


class SnmpTypes(db.Model):
    __tablename__ = 'snmp_types'

    ID: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    TYPE_NAME: Mapped[str] = mapped_column(String(255), nullable=False)
    TABLE_TYPE_NAME: Mapped[str] = mapped_column(String(255), nullable=False)


class SnmpTypesConditions(db.Model):
    __tablename__ = 'snmp_types_conditions'

    ID: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    TYPE_ID: Mapped[int] = mapped_column(INTEGER(11), nullable=False)
    CONDITION_OID: Mapped[str] = mapped_column(VARCHAR(255, charset='utf8mb4', collation='utf8mb4_general_ci'), nullable=False)
    CONDITION_VALUE: Mapped[Optional[str]] = mapped_column(VARCHAR(255, charset='utf8mb4', collation='utf8mb4_general_ci'))


class Software(db.Model):
    __tablename__ = 'software'
    __table_args__ = (
        Index('HARDWARE_ID', 'HARDWARE_ID'),
        Index('HARDWARE_ID_2', 'HARDWARE_ID', 'NAME_ID', 'VERSION_ID'),
        Index('NAME_ID', 'NAME_ID'),
        Index('PUBLISHER_ID', 'PUBLISHER_ID'),
        Index('VERSION_ID', 'VERSION_ID')
    )

    ID: Mapped[int] = mapped_column(BIGINT(20), primary_key=True)
    HARDWARE_ID: Mapped[int] = mapped_column(INTEGER(11), ForeignKey('hardware.ID'), nullable=False)
    NAME_ID: Mapped[int] = mapped_column(INTEGER(11), ForeignKey('software_name.ID'), nullable=False)
    PUBLISHER_ID: Mapped[int] = mapped_column(INTEGER(11), ForeignKey('software_publisher.ID'), nullable=False)
    VERSION_ID: Mapped[int] = mapped_column(INTEGER(11), ForeignKey('software_version.ID'), nullable=False)
    FOLDER: Mapped[Optional[str]] = mapped_column(Text)
    COMMENTS: Mapped[Optional[str]] = mapped_column(Text)
    FILENAME: Mapped[Optional[str]] = mapped_column(String(255))
    FILESIZE: Mapped[Optional[int]] = mapped_column(INTEGER(11), server_default=text('0'))
    SOURCE: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    GUID: Mapped[Optional[str]] = mapped_column(String(255))
    LANGUAGE: Mapped[Optional[str]] = mapped_column(String(255))
    INSTALLDATE: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    BITSWIDTH: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    ARCHITECTURE: Mapped[Optional[str]] = mapped_column(String(255))

    hardware : Mapped['Hardware'] = relationship('Hardware')
    software_name : Mapped['SoftwareName'] = relationship('SoftwareName')
    software_publisher : Mapped['SoftwarePublisher'] = relationship('SoftwarePublisher')
    software_version : Mapped['SoftwareVersion'] = relationship('SoftwareVersion')


class SoftwareCategories(db.Model):
    __tablename__ = 'software_categories'

    ID: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    CATEGORY_NAME: Mapped[str] = mapped_column(String(255), nullable=False)
    OS: Mapped[Optional[str]] = mapped_column(String(255))


class SoftwareCategoriesLink(db.Model):
    __tablename__ = 'software_categories_link'
    __table_args__ = (
        Index('CATEGORY_ID', 'CATEGORY_ID'),
        Index('NAME_ID', 'NAME_ID'),
        Index('PUBLISHER_ID', 'PUBLISHER_ID'),
        Index('VERSION_ID', 'VERSION_ID')
    )

    ID: Mapped[int] = mapped_column(BIGINT(20), primary_key=True)
    NAME_ID: Mapped[int] = mapped_column(INTEGER(11), nullable=False)
    PUBLISHER_ID: Mapped[int] = mapped_column(INTEGER(11), nullable=False)
    VERSION_ID: Mapped[int] = mapped_column(INTEGER(11), nullable=False)
    CATEGORY_ID: Mapped[int] = mapped_column(INTEGER(11), nullable=False)


class SoftwareCategoryExp(db.Model):
    __tablename__ = 'software_category_exp'
    __table_args__ = (
        Index('CATEGORY_ID', 'CATEGORY_ID'),
    )

    CATEGORY_ID: Mapped[int] = mapped_column(INTEGER(11), nullable=False)
    SOFTWARE_EXP: Mapped[str] = mapped_column(String(255), nullable=False)
    ID: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    SIGN_VERSION: Mapped[Optional[str]] = mapped_column(String(255))
    VERSION: Mapped[Optional[str]] = mapped_column(String(255))
    PUBLISHER: Mapped[Optional[str]] = mapped_column(String(255))


class SoftwareLink(db.Model):
    __tablename__ = 'software_link'
    __table_args__ = (
        Index('NAME_ID', 'NAME_ID'),
        Index('PUBLISHER_ID', 'PUBLISHER_ID'),
        Index('VERSION_ID', 'VERSION_ID')
    )

    ID: Mapped[int] = mapped_column(BIGINT(20), primary_key=True)
    NAME_ID: Mapped[int] = mapped_column(INTEGER(11), nullable=False)
    PUBLISHER_ID: Mapped[int] = mapped_column(INTEGER(11), nullable=False)
    VERSION_ID: Mapped[int] = mapped_column(INTEGER(11), nullable=False)
    IDENTIFIER: Mapped[str] = mapped_column(VARCHAR(255, charset='utf8mb4', collation='utf8mb4_general_ci'), nullable=False)
    CATEGORY_ID: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    COUNT: Mapped[Optional[int]] = mapped_column(INTEGER(11))


class SoftwareName(db.Model):
    __tablename__ = 'software_name'
    __table_args__ = (
        Index('NAME', 'NAME', unique=True),
    )

    ID: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    NAME: Mapped[str] = mapped_column(String(255), nullable=False)



class SoftwarePublisher(db.Model):
    __tablename__ = 'software_publisher'
    __table_args__ = (
        Index('PUBLISHER', 'PUBLISHER', unique=True),
    )

    ID: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    PUBLISHER: Mapped[str] = mapped_column(String(255), nullable=False)


class SoftwareVersion(db.Model):
    __tablename__ = 'software_version'
    __table_args__ = (
        Index('VERSION', 'VERSION', unique=True),
        Index('index_prettyversion', 'PRETTYVERSION')
    )

    ID: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    VERSION: Mapped[str] = mapped_column(String(255), nullable=False)
    PRETTYVERSION: Mapped[Optional[str]] = mapped_column(String(255))
    MAJOR: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    MINOR: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    PATCH: Mapped[Optional[int]] = mapped_column(INTEGER(11))


class SoftwaresNameCache(db.Model):
    __tablename__ = 'softwares_name_cache'
    __table_args__ = (
        Index('NAME', 'NAME', unique=True),
    )

    ID: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    NAME: Mapped[Optional[str]] = mapped_column(String(255))


class Sounds(db.Model):
    __tablename__ = 'sounds'
    __table_args__ = (
        Index('HARDWARE_ID', 'HARDWARE_ID'),
    )

    ID: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    HARDWARE_ID: Mapped[int] = mapped_column(INTEGER(11), nullable=False)
    MANUFACTURER: Mapped[Optional[str]] = mapped_column(String(255))
    NAME: Mapped[Optional[str]] = mapped_column(String(255))
    DESCRIPTION: Mapped[Optional[str]] = mapped_column(String(255))


class SslStore(db.Model):
    __tablename__ = 'ssl_store'

    ID: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    FILE: Mapped[Optional[bytes]] = mapped_column(LONGBLOB)
    AUTHOR: Mapped[Optional[str]] = mapped_column(String(255))
    FILE_NAME: Mapped[Optional[str]] = mapped_column(String(255))
    FILE_TYPE: Mapped[Optional[str]] = mapped_column(String(20))
    DESCRIPTION: Mapped[Optional[str]] = mapped_column(String(255))


class Storages(db.Model):
    __tablename__ = 'storages'
    __table_args__ = (
        Index('HARDWARE_ID', 'HARDWARE_ID'),
    )

    ID: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    HARDWARE_ID: Mapped[int] = mapped_column(INTEGER(11), nullable=False)
    MANUFACTURER: Mapped[Optional[str]] = mapped_column(String(255))
    NAME: Mapped[Optional[str]] = mapped_column(String(255))
    MODEL: Mapped[Optional[str]] = mapped_column(String(255))
    DESCRIPTION: Mapped[Optional[str]] = mapped_column(String(255))
    TYPE: Mapped[Optional[str]] = mapped_column(String(255))
    DISKSIZE: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    SERIALNUMBER: Mapped[Optional[str]] = mapped_column(String(255))
    FIRMWARE: Mapped[Optional[str]] = mapped_column(String(255))


class Subnet(db.Model):
    __tablename__ = 'subnet'
    __table_args__ = (
        Index('ID', 'ID'),
    )

    PK: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    NETID: Mapped[str] = mapped_column(String(15), nullable=False)
    NAME: Mapped[Optional[str]] = mapped_column(String(255))
    ID: Mapped[Optional[str]] = mapped_column(String(255))
    MASK: Mapped[Optional[str]] = mapped_column(String(255))
    TAG: Mapped[Optional[str]] = mapped_column(String(255))


class Tags(db.Model):
    __tablename__ = 'tags'
    __table_args__ = (
        Index('Login', 'Login'),
        Index('Tag', 'Tag')
    )

    Tag: Mapped[str] = mapped_column(String(100), primary_key=True, server_default=text("''"))
    Login: Mapped[str] = mapped_column(String(100), primary_key=True, server_default=text("''"))


class TempFiles(db.Model):
    __tablename__ = 'temp_files'

    ID: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    TABLE_NAME: Mapped[Optional[str]] = mapped_column(String(255))
    FIELDS_NAME: Mapped[Optional[str]] = mapped_column(String(255))
    file: Mapped[Optional[bytes]] = mapped_column(LONGBLOB)
    COMMENT: Mapped[Optional[str]] = mapped_column(LONGTEXT)
    AUTHOR: Mapped[Optional[str]] = mapped_column(String(255))
    FILE_NAME: Mapped[Optional[str]] = mapped_column(String(255))
    FILE_TYPE: Mapped[Optional[str]] = mapped_column(String(255))
    FILE_SIZE: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    ID_DDE: Mapped[Optional[int]] = mapped_column(INTEGER(11))


class Usbdevices(db.Model):
    __tablename__ = 'usbdevices'
    __table_args__ = (
        Index('HARDWARE_ID', 'HARDWARE_ID'),
    )

    ID: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    HARDWARE_ID: Mapped[int] = mapped_column(INTEGER(11), nullable=False)
    DESCRIPTION: Mapped[Optional[str]] = mapped_column(String(255))
    INTERFACE: Mapped[Optional[str]] = mapped_column(String(255))
    MANUFACTURER: Mapped[Optional[str]] = mapped_column(String(255))
    SERIAL: Mapped[Optional[str]] = mapped_column(String(255))
    TYPE: Mapped[Optional[str]] = mapped_column(String(255))


class Videos(db.Model):
    __tablename__ = 'videos'
    __table_args__ = (
        Index('HARDWARE_ID', 'HARDWARE_ID'),
    )

    ID: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    HARDWARE_ID: Mapped[int] = mapped_column(INTEGER(11), nullable=False)
    NAME: Mapped[Optional[str]] = mapped_column(String(255))
    CHIPSET: Mapped[Optional[str]] = mapped_column(String(255))
    MEMORY: Mapped[Optional[str]] = mapped_column(String(255))
    RESOLUTION: Mapped[Optional[str]] = mapped_column(String(255))


class Virtualmachines(db.Model):
    __tablename__ = 'virtualmachines'
    __table_args__ = (
        Index('HARDWARE_ID', 'HARDWARE_ID'),
    )

    ID: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    HARDWARE_ID: Mapped[int] = mapped_column(INTEGER(11), nullable=False)
    NAME: Mapped[Optional[str]] = mapped_column(String(255))
    STATUS: Mapped[Optional[str]] = mapped_column(String(255))
    SUBSYSTEM: Mapped[Optional[str]] = mapped_column(String(255))
    VMTYPE: Mapped[Optional[str]] = mapped_column(String(255))
    UUID: Mapped[Optional[str]] = mapped_column(String(255))
    VCPU: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    MEMORY: Mapped[Optional[int]] = mapped_column(INTEGER(11))


class Archive(db.Model):
    __tablename__ = 'archive'
    __table_args__ = (
        ForeignKeyConstraint(['HARDWARE_ID'], ['hardware.ID'], name='archive_ibfk_1'),
        Index('HARDWARE_ID', 'HARDWARE_ID', unique=True)
    )

    ID: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    HARDWARE_ID: Mapped[int] = mapped_column(INTEGER(11), nullable=False)

    hardware: Mapped['Hardware'] = relationship('Hardware', back_populates='archive')
