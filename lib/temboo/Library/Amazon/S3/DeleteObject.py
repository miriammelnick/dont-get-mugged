
###############################################################################
#
# DeleteObject
# Deletes a specified item from an Amazon S3 bucket.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class DeleteObject(Choreography):

    """
    Create a new instance of the DeleteObject Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Amazon/S3/DeleteObject')


    def new_input_set(self):
        return DeleteObjectInputSet()

    def _make_result_set(self, result, path):
        return DeleteObjectResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DeleteObjectChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the DeleteObject
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class DeleteObjectInputSet(InputSet):
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
        Set the value of the BucketName input for this choreography. ((required, string) The the name of the bucket that contains the object that you want to delete.)
        """
        def set_BucketName(self, value):
            InputSet._set_input(self, 'BucketName', value)

        """
        Set the value of the FileName input for this choreography. ((required, string) The file name that you want to delete.)
        """
        def set_FileName(self, value):
            InputSet._set_input(self, 'FileName', value)


"""
A ResultSet with methods tailored to the values returned by the DeleteObject choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class DeleteObjectResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from Amazon. Note that no content is returned for a successful delete operation.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class DeleteObjectChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return DeleteObjectResultSet(response, path)
