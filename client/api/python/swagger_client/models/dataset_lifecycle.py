# coding: utf-8

"""
    dacat-api

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 2.5.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class DatasetLifecycle(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, isOnDisk=None, isOnTape=None, archiveStatusMessage=None, retrieveStatusMessage=None, dateOfLastMessage=None, dateOfDiskPurging=None, archiveRetentionTime=None, isExported=None, exportedTo=None, dateOfPublishing=None, datasetId=None, rawDatasetId=None, derivedDatasetId=None, createdAt=None, updatedAt=None):
        """
        DatasetLifecycle - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'isOnDisk': 'bool',
            'isOnTape': 'bool',
            'archiveStatusMessage': 'str',
            'retrieveStatusMessage': 'str',
            'dateOfLastMessage': 'datetime',
            'dateOfDiskPurging': 'datetime',
            'archiveRetentionTime': 'datetime',
            'isExported': 'bool',
            'exportedTo': 'str',
            'dateOfPublishing': 'datetime',
            'datasetId': 'str',
            'rawDatasetId': 'str',
            'derivedDatasetId': 'str',
            'createdAt': 'datetime',
            'updatedAt': 'datetime'
        }

        self.attribute_map = {
            'id': 'id',
            'isOnDisk': 'isOnDisk',
            'isOnTape': 'isOnTape',
            'archiveStatusMessage': 'archiveStatusMessage',
            'retrieveStatusMessage': 'retrieveStatusMessage',
            'dateOfLastMessage': 'dateOfLastMessage',
            'dateOfDiskPurging': 'dateOfDiskPurging',
            'archiveRetentionTime': 'archiveRetentionTime',
            'isExported': 'isExported',
            'exportedTo': 'exportedTo',
            'dateOfPublishing': 'dateOfPublishing',
            'datasetId': 'datasetId',
            'rawDatasetId': 'rawDatasetId',
            'derivedDatasetId': 'derivedDatasetId',
            'createdAt': 'createdAt',
            'updatedAt': 'updatedAt'
        }

        self._id = id
        self._isOnDisk = isOnDisk
        self._isOnTape = isOnTape
        self._archiveStatusMessage = archiveStatusMessage
        self._retrieveStatusMessage = retrieveStatusMessage
        self._dateOfLastMessage = dateOfLastMessage
        self._dateOfDiskPurging = dateOfDiskPurging
        self._archiveRetentionTime = archiveRetentionTime
        self._isExported = isExported
        self._exportedTo = exportedTo
        self._dateOfPublishing = dateOfPublishing
        self._datasetId = datasetId
        self._rawDatasetId = rawDatasetId
        self._derivedDatasetId = derivedDatasetId
        self._createdAt = createdAt
        self._updatedAt = updatedAt

    @property
    def id(self):
        """
        Gets the id of this DatasetLifecycle.
        ID of status information. This must be the ID of the associated dataset

        :return: The id of this DatasetLifecycle.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this DatasetLifecycle.
        ID of status information. This must be the ID of the associated dataset

        :param id: The id of this DatasetLifecycle.
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id

    @property
    def isOnDisk(self):
        """
        Gets the isOnDisk of this DatasetLifecycle.
        Flag which is true, if full dataset is available on disk

        :return: The isOnDisk of this DatasetLifecycle.
        :rtype: bool
        """
        return self._isOnDisk

    @isOnDisk.setter
    def isOnDisk(self, isOnDisk):
        """
        Sets the isOnDisk of this DatasetLifecycle.
        Flag which is true, if full dataset is available on disk

        :param isOnDisk: The isOnDisk of this DatasetLifecycle.
        :type: bool
        """

        self._isOnDisk = isOnDisk

    @property
    def isOnTape(self):
        """
        Gets the isOnTape of this DatasetLifecycle.
        Flag which is true, if full dataset has been stored to tape

        :return: The isOnTape of this DatasetLifecycle.
        :rtype: bool
        """
        return self._isOnTape

    @isOnTape.setter
    def isOnTape(self, isOnTape):
        """
        Sets the isOnTape of this DatasetLifecycle.
        Flag which is true, if full dataset has been stored to tape

        :param isOnTape: The isOnTape of this DatasetLifecycle.
        :type: bool
        """

        self._isOnTape = isOnTape

    @property
    def archiveStatusMessage(self):
        """
        Gets the archiveStatusMessage of this DatasetLifecycle.
        Latest status update message for this dataset from archive system, e.g. archive-in-progress,  60%-stored-on-tape etc

        :return: The archiveStatusMessage of this DatasetLifecycle.
        :rtype: str
        """
        return self._archiveStatusMessage

    @archiveStatusMessage.setter
    def archiveStatusMessage(self, archiveStatusMessage):
        """
        Sets the archiveStatusMessage of this DatasetLifecycle.
        Latest status update message for this dataset from archive system, e.g. archive-in-progress,  60%-stored-on-tape etc

        :param archiveStatusMessage: The archiveStatusMessage of this DatasetLifecycle.
        :type: str
        """

        self._archiveStatusMessage = archiveStatusMessage

    @property
    def retrieveStatusMessage(self):
        """
        Gets the retrieveStatusMessage of this DatasetLifecycle.
        Latest status update message for this dataset concerning retrieve from archive system

        :return: The retrieveStatusMessage of this DatasetLifecycle.
        :rtype: str
        """
        return self._retrieveStatusMessage

    @retrieveStatusMessage.setter
    def retrieveStatusMessage(self, retrieveStatusMessage):
        """
        Sets the retrieveStatusMessage of this DatasetLifecycle.
        Latest status update message for this dataset concerning retrieve from archive system

        :param retrieveStatusMessage: The retrieveStatusMessage of this DatasetLifecycle.
        :type: str
        """

        self._retrieveStatusMessage = retrieveStatusMessage

    @property
    def dateOfLastMessage(self):
        """
        Gets the dateOfLastMessage of this DatasetLifecycle.
        Time when last status message was sent. Format according to chapter 5.6 internet date/time format in RFC 3339. This will be filled automatically if not provided

        :return: The dateOfLastMessage of this DatasetLifecycle.
        :rtype: datetime
        """
        return self._dateOfLastMessage

    @dateOfLastMessage.setter
    def dateOfLastMessage(self, dateOfLastMessage):
        """
        Sets the dateOfLastMessage of this DatasetLifecycle.
        Time when last status message was sent. Format according to chapter 5.6 internet date/time format in RFC 3339. This will be filled automatically if not provided

        :param dateOfLastMessage: The dateOfLastMessage of this DatasetLifecycle.
        :type: datetime
        """

        self._dateOfLastMessage = dateOfLastMessage

    @property
    def dateOfDiskPurging(self):
        """
        Gets the dateOfDiskPurging of this DatasetLifecycle.
        Time when dataset will be removed from disk, assuming that is already stored on tape. Format according to chapter 5.6 internet date/time format in RFC 3339

        :return: The dateOfDiskPurging of this DatasetLifecycle.
        :rtype: datetime
        """
        return self._dateOfDiskPurging

    @dateOfDiskPurging.setter
    def dateOfDiskPurging(self, dateOfDiskPurging):
        """
        Sets the dateOfDiskPurging of this DatasetLifecycle.
        Time when dataset will be removed from disk, assuming that is already stored on tape. Format according to chapter 5.6 internet date/time format in RFC 3339

        :param dateOfDiskPurging: The dateOfDiskPurging of this DatasetLifecycle.
        :type: datetime
        """

        self._dateOfDiskPurging = dateOfDiskPurging

    @property
    def archiveRetentionTime(self):
        """
        Gets the archiveRetentionTime of this DatasetLifecycle.
        When the dataset's future fate will be evaluated again, e.g. to decide if the dataset can be deleted from archive. Format according to chapter 5.6 internet date/time format in RFC 3339

        :return: The archiveRetentionTime of this DatasetLifecycle.
        :rtype: datetime
        """
        return self._archiveRetentionTime

    @archiveRetentionTime.setter
    def archiveRetentionTime(self, archiveRetentionTime):
        """
        Sets the archiveRetentionTime of this DatasetLifecycle.
        When the dataset's future fate will be evaluated again, e.g. to decide if the dataset can be deleted from archive. Format according to chapter 5.6 internet date/time format in RFC 3339

        :param archiveRetentionTime: The archiveRetentionTime of this DatasetLifecycle.
        :type: datetime
        """

        self._archiveRetentionTime = archiveRetentionTime

    @property
    def isExported(self):
        """
        Gets the isExported of this DatasetLifecycle.
        Flag is true if data was exported to another location

        :return: The isExported of this DatasetLifecycle.
        :rtype: bool
        """
        return self._isExported

    @isExported.setter
    def isExported(self, isExported):
        """
        Sets the isExported of this DatasetLifecycle.
        Flag is true if data was exported to another location

        :param isExported: The isExported of this DatasetLifecycle.
        :type: bool
        """

        self._isExported = isExported

    @property
    def exportedTo(self):
        """
        Gets the exportedTo of this DatasetLifecycle.
        Location of the export destination

        :return: The exportedTo of this DatasetLifecycle.
        :rtype: str
        """
        return self._exportedTo

    @exportedTo.setter
    def exportedTo(self, exportedTo):
        """
        Sets the exportedTo of this DatasetLifecycle.
        Location of the export destination

        :param exportedTo: The exportedTo of this DatasetLifecycle.
        :type: str
        """

        self._exportedTo = exportedTo

    @property
    def dateOfPublishing(self):
        """
        Gets the dateOfPublishing of this DatasetLifecycle.
        Date when dataset is supposed to become public according to data policy

        :return: The dateOfPublishing of this DatasetLifecycle.
        :rtype: datetime
        """
        return self._dateOfPublishing

    @dateOfPublishing.setter
    def dateOfPublishing(self, dateOfPublishing):
        """
        Sets the dateOfPublishing of this DatasetLifecycle.
        Date when dataset is supposed to become public according to data policy

        :param dateOfPublishing: The dateOfPublishing of this DatasetLifecycle.
        :type: datetime
        """

        self._dateOfPublishing = dateOfPublishing

    @property
    def datasetId(self):
        """
        Gets the datasetId of this DatasetLifecycle.

        :return: The datasetId of this DatasetLifecycle.
        :rtype: str
        """
        return self._datasetId

    @datasetId.setter
    def datasetId(self, datasetId):
        """
        Sets the datasetId of this DatasetLifecycle.

        :param datasetId: The datasetId of this DatasetLifecycle.
        :type: str
        """

        self._datasetId = datasetId

    @property
    def rawDatasetId(self):
        """
        Gets the rawDatasetId of this DatasetLifecycle.

        :return: The rawDatasetId of this DatasetLifecycle.
        :rtype: str
        """
        return self._rawDatasetId

    @rawDatasetId.setter
    def rawDatasetId(self, rawDatasetId):
        """
        Sets the rawDatasetId of this DatasetLifecycle.

        :param rawDatasetId: The rawDatasetId of this DatasetLifecycle.
        :type: str
        """

        self._rawDatasetId = rawDatasetId

    @property
    def derivedDatasetId(self):
        """
        Gets the derivedDatasetId of this DatasetLifecycle.

        :return: The derivedDatasetId of this DatasetLifecycle.
        :rtype: str
        """
        return self._derivedDatasetId

    @derivedDatasetId.setter
    def derivedDatasetId(self, derivedDatasetId):
        """
        Sets the derivedDatasetId of this DatasetLifecycle.

        :param derivedDatasetId: The derivedDatasetId of this DatasetLifecycle.
        :type: str
        """

        self._derivedDatasetId = derivedDatasetId

    @property
    def createdAt(self):
        """
        Gets the createdAt of this DatasetLifecycle.

        :return: The createdAt of this DatasetLifecycle.
        :rtype: datetime
        """
        return self._createdAt

    @createdAt.setter
    def createdAt(self, createdAt):
        """
        Sets the createdAt of this DatasetLifecycle.

        :param createdAt: The createdAt of this DatasetLifecycle.
        :type: datetime
        """

        self._createdAt = createdAt

    @property
    def updatedAt(self):
        """
        Gets the updatedAt of this DatasetLifecycle.

        :return: The updatedAt of this DatasetLifecycle.
        :rtype: datetime
        """
        return self._updatedAt

    @updatedAt.setter
    def updatedAt(self, updatedAt):
        """
        Sets the updatedAt of this DatasetLifecycle.

        :param updatedAt: The updatedAt of this DatasetLifecycle.
        :type: datetime
        """

        self._updatedAt = updatedAt

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, DatasetLifecycle):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
