
###############################################################################
#
# PutBucketLifecycle
# Sets lifecycle configuration for your bucket. This is used to remove objects from a bucket automatically after a certain time.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class PutBucketLifecycle(Choreography):

    """
    Create a new instance of the PutBucketLifecycle Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Amazon/S3/PutBucketLifecycle')


    def new_input_set(self):
        return PutBucketLifecycleInputSet()

    def _make_result_set(self, result, path):
        return PutBucketLifecycleResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return PutBucketLifecycleChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the PutBucketLifecycle
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class PutBucketLifecycleInputSet(InputSet):
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
        Set the value of the LifecycleId input for this choreography. ((optional, string) A unique ID for this lifecycle (i.e. delete-logs-in-30-days-rule).)
        """
        def set_LifecycleId(self, value):
            InputSet._set_input(self, 'LifecycleId', value)

        """
        Set the value of the NumberOfDays input for this choreography. ((required, integer) The number of days until this lifecycle expires.)
        """
        def set_NumberOfDays(self, value):
            InputSet._set_input(self, 'NumberOfDays', value)

        """
        Set the value of the Prefix input for this choreography. ((optional, string) Indicating that objects with this prefix will expire and be removed after the number of days specified. If not specified this lifecycle will apply to all objects in the bucket.)
        """
        def set_Prefix(self, value):
            InputSet._set_input(self, 'Prefix', value)

        """
        Set the value of the Status input for this choreography. ((optional, string) The lifecycle status. Accepted values are: "Enabled" or "Disabled". Defaults to "Enabled".)
        """
        def set_Status(self, value):
            InputSet._set_input(self, 'Status', value)


"""
A ResultSet with methods tailored to the values returned by the PutBucketLifecycle choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class PutBucketLifecycleResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) Stores the response from Amazon. Note that for a successful lifecycle creation, no content is returned and this output variable should be empty.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class PutBucketLifecycleChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return PutBucketLifecycleResultSet(response, path)
