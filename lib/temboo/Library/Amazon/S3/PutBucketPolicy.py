
###############################################################################
#
# PutBucketPolicy
# Allows you to add to or replace a policy on a bucket.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class PutBucketPolicy(Choreography):

    """
    Create a new instance of the PutBucketPolicy Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Amazon/S3/PutBucketPolicy')


    def new_input_set(self):
        return PutBucketPolicyInputSet()

    def _make_result_set(self, result, path):
        return PutBucketPolicyResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return PutBucketPolicyChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the PutBucketPolicy
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class PutBucketPolicyInputSet(InputSet):
        """
        Set the value of the Policy input for this choreography. ((required, json) A JSON string containing the policy information.  See Choreo documentation for a sample JSON policy.)
        """
        def set_Policy(self, value):
            InputSet._set_input(self, 'Policy', value)

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
        Set the value of the BucketName input for this choreography. ((required, string) The name of the bucket to create or update a policy for.)
        """
        def set_BucketName(self, value):
            InputSet._set_input(self, 'BucketName', value)


"""
A ResultSet with methods tailored to the values returned by the PutBucketPolicy choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class PutBucketPolicyResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) Stores the response from Amazon. Note that for a successful policy creation, no content is returned and this output variable should be empty.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class PutBucketPolicyChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return PutBucketPolicyResultSet(response, path)
