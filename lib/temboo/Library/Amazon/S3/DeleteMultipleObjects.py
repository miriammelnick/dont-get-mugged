
###############################################################################
#
# DeleteMultipleObjects
# Deletes multiple objects from an S3 Bucket.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class DeleteMultipleObjects(Choreography):

    """
    Create a new instance of the DeleteMultipleObjects Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Amazon/S3/DeleteMultipleObjects')


    def new_input_set(self):
        return DeleteMultipleObjectsInputSet()

    def _make_result_set(self, result, path):
        return DeleteMultipleObjectsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DeleteMultipleObjectsChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the DeleteMultipleObjects
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class DeleteMultipleObjectsInputSet(InputSet):
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
        Set the value of the BucketName input for this choreography. ((required, string) The the name of the bucket that contains the objects that you want to delete.)
        """
        def set_BucketName(self, value):
            InputSet._set_input(self, 'BucketName', value)

        """
        Set the value of the FileNames input for this choreography. ((required, string) A list of file names to delete (separated by commas).)
        """
        def set_FileNames(self, value):
            InputSet._set_input(self, 'FileNames', value)


"""
A ResultSet with methods tailored to the values returned by the DeleteMultipleObjects choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class DeleteMultipleObjectsResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from Amazon. Note that no content is returned for a successful delete operation.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class DeleteMultipleObjectsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return DeleteMultipleObjectsResultSet(response, path)
