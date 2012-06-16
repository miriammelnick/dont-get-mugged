
###############################################################################
#
# CopyObject
# Makes a copy of an existing object in S3 Storage.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class CopyObject(Choreography):

    """
    Create a new instance of the CopyObject Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Amazon/S3/CopyObject')


    def new_input_set(self):
        return CopyObjectInputSet()

    def _make_result_set(self, result, path):
        return CopyObjectResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CopyObjectChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the CopyObject
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class CopyObjectInputSet(InputSet):
        """
        Set the value of the AWSAccessKeyId input for this choreography. ((required, string) The Access Key ID provided by Amazon Web Services.)
        """
        def set_AWSAccessKeyId(self, value):
            InputSet._set_input(self, 'AWSAccessKeyId', value)

        """
        Set the value of the AWSSecretKeyId input for this choreography. ((required, string) The Secret Key ID provided by Amazon Web Services.)
        """
        def set_AWSSecretKeyId(self, value):
            InputSet._set_input(self, 'AWSSecretKeyId', value)

        """
        Set the value of the BucketName input for this choreography. ((required, string) The name of the bucket that will be the file destination.)
        """
        def set_BucketName(self, value):
            InputSet._set_input(self, 'BucketName', value)

        """
        Set the value of the FileToCopy input for this choreography. ((required, string) The name of the file to copy.)
        """
        def set_FileToCopy(self, value):
            InputSet._set_input(self, 'FileToCopy', value)

        """
        Set the value of the NewFileName input for this choreography. ((required, string) The file name for the new copy.)
        """
        def set_NewFileName(self, value):
            InputSet._set_input(self, 'NewFileName', value)

        """
        Set the value of the VaultFile input for this choreography. ((optional, vault file) The path to a vault file that you want to upload to an Amazon S3 bucket. Required unless using the FileContents input variable.)
        """


"""
A ResultSet with methods tailored to the values returned by the CopyObject choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class CopyObjectResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from Amazon. Note that no content is returned for successful uploads.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class CopyObjectChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return CopyObjectResultSet(response, path)
