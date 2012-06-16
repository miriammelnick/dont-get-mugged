
###############################################################################
#
# GetBucketLifecycle
# Returns the lifecycle configuration information set on the bucket.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetBucketLifecycle(Choreography):

    """
    Create a new instance of the GetBucketLifecycle Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Amazon/S3/GetBucketLifecycle')


    def new_input_set(self):
        return GetBucketLifecycleInputSet()

    def _make_result_set(self, result, path):
        return GetBucketLifecycleResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetBucketLifecycleChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetBucketLifecycle
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetBucketLifecycleInputSet(InputSet):
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
        Set the value of the BucketName input for this choreography. ((required, string) The name of the bucket associated with the lifecycle you want to retrieve.)
        """
        def set_BucketName(self, value):
            InputSet._set_input(self, 'BucketName', value)


"""
A ResultSet with methods tailored to the values returned by the GetBucketLifecycle choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetBucketLifecycleResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((json) The response from Amazon.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetBucketLifecycleChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetBucketLifecycleResultSet(response, path)
