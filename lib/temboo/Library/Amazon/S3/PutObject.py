
###############################################################################
#
# PutObject
# Uploads a file to your Amazon S3 storage bucket.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class PutObject(Choreography):

    """
    Create a new instance of the PutObject Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Amazon/S3/PutObject')


    def new_input_set(self):
        return PutObjectInputSet()

    def _make_result_set(self, result, path):
        return PutObjectResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return PutObjectChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the PutObject
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class PutObjectInputSet(InputSet):
        """
        Set the value of the FileContents input for this choreography. ((conditional, string) The base64 encoded file contents that you want to upload to an AmazonS3 bucket. Required unless using the VaultFile input alias (an advanced option when using the Temboo Designer to execute Choreos).)
        """
        def set_FileContents(self, value):
            InputSet._set_input(self, 'FileContents', value)

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
        Set the value of the FileName input for this choreography. ((required, string) The name of the file to put in S3 Storage.)
        """
        def set_FileName(self, value):
            InputSet._set_input(self, 'FileName', value)

        """
        Set the value of the VaultFile input for this choreography. ((optional, vault file) The path to a vault file that you want to upload to an Amazon S3 bucket. Required unless using the FileContents input variable.)
        """


"""
A ResultSet with methods tailored to the values returned by the PutObject choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class PutObjectResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from Amazon. Note that no content is returned for successful uploads.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class PutObjectChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return PutObjectResultSet(response, path)
