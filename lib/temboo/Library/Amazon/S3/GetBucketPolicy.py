
###############################################################################
#
# GetBucketPolicy
# Returns the policy of a specified bucket.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetBucketPolicy(Choreography):

    """
    Create a new instance of the GetBucketPolicy Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Amazon/S3/GetBucketPolicy')


    def new_input_set(self):
        return GetBucketPolicyInputSet()

    def _make_result_set(self, result, path):
        return GetBucketPolicyResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetBucketPolicyChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetBucketPolicy
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetBucketPolicyInputSet(InputSet):
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
        Set the value of the BucketName input for this choreography. ((required, string) The name of the bucket associated with the policy you want to retrieve.)
        """
        def set_BucketName(self, value):
            InputSet._set_input(self, 'BucketName', value)


"""
A ResultSet with methods tailored to the values returned by the GetBucketPolicy choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetBucketPolicyResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((json) The response from Amazon.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetBucketPolicyChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetBucketPolicyResultSet(response, path)
