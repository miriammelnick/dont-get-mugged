
###############################################################################
#
# GetBase64EncodedObject
# Retrieves a specified item from an Amazon S3 bucket, and returns the file content as base64-encoded data.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetBase64EncodedObject(Choreography):

    """
    Create a new instance of the GetBase64EncodedObject Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Amazon/S3/GetBase64EncodedObject')


    def new_input_set(self):
        return GetBase64EncodedObjectInputSet()

    def _make_result_set(self, result, path):
        return GetBase64EncodedObjectResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetBase64EncodedObjectChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetBase64EncodedObject
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetBase64EncodedObjectInputSet(InputSet):
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
        Set the value of the BucketName input for this choreography. ((required, string) The name of the bucket that contains the object to retrieve.)
        """
        def set_BucketName(self, value):
            InputSet._set_input(self, 'BucketName', value)

        """
        Set the value of the FileName input for this choreography. ((required, string) The name of the file to retrieve.)
        """
        def set_FileName(self, value):
            InputSet._set_input(self, 'FileName', value)


"""
A ResultSet with methods tailored to the values returned by the GetBase64EncodedObject choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetBase64EncodedObjectResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((string) The base64-encoded contents of the file you are retrieving.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetBase64EncodedObjectChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetBase64EncodedObjectResultSet(response, path)
