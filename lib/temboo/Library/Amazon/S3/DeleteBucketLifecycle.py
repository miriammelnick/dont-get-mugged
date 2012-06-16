
###############################################################################
#
# DeleteBucketLifecycle
# Deletes the lifecycle configuration from the specified bucket.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class DeleteBucketLifecycle(Choreography):

    """
    Create a new instance of the DeleteBucketLifecycle Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Amazon/S3/DeleteBucketLifecycle')


    def new_input_set(self):
        return DeleteBucketLifecycleInputSet()

    def _make_result_set(self, result, path):
        return DeleteBucketLifecycleResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DeleteBucketLifecycleChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the DeleteBucketLifecycle
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class DeleteBucketLifecycleInputSet(InputSet):
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
        Set the value of the BucketName input for this choreography. ((required, string) The name of the bucket associated with the lifecycle you want to delete.)
        """
        def set_BucketName(self, value):
            InputSet._set_input(self, 'BucketName', value)


"""
A ResultSet with methods tailored to the values returned by the DeleteBucketLifecycle choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class DeleteBucketLifecycleResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) Stores the response from Amazon. Note that for a successful delete operation, no content is returned, and this output variable should be empty.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class DeleteBucketLifecycleChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return DeleteBucketLifecycleResultSet(response, path)
