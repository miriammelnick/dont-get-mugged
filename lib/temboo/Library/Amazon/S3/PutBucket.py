
###############################################################################
#
# PutBucket
# Creates a new bucket in your Amazon S3 account.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class PutBucket(Choreography):

    """
    Create a new instance of the PutBucket Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Amazon/S3/PutBucket')


    def new_input_set(self):
        return PutBucketInputSet()

    def _make_result_set(self, result, path):
        return PutBucketResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return PutBucketChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the PutBucket
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class PutBucketInputSet(InputSet):
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
        Set the value of the BucketName input for this choreography. ((required, string) The name of the bucket that will be created.)
        """
        def set_BucketName(self, value):
            InputSet._set_input(self, 'BucketName', value)

        """
        Set the value of the LocationConstraint input for this choreography. ((optional, string) The region to create the bucket in. Valid Values: EU, us-west-1, ap-southeast-1, ap-northeast-1. Defaults to US Classic Region when empty.)
        """
        def set_LocationConstraint(self, value):
            InputSet._set_input(self, 'LocationConstraint', value)


"""
A ResultSet with methods tailored to the values returned by the PutBucket choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class PutBucketResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from Amazon. Note that no content is returned for successful uploads.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class PutBucketChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return PutBucketResultSet(response, path)
