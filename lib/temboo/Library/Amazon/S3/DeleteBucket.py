
###############################################################################
#
# DeleteBucket
# Deletes a bucket from your Amazon S3 account.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class DeleteBucket(Choreography):

    """
    Create a new instance of the DeleteBucket Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Amazon/S3/DeleteBucket')


    def new_input_set(self):
        return DeleteBucketInputSet()

    def _make_result_set(self, result, path):
        return DeleteBucketResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DeleteBucketChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the DeleteBucket
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class DeleteBucketInputSet(InputSet):
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
A ResultSet with methods tailored to the values returned by the DeleteBucket choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class DeleteBucketResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from Amazon. Note that no content is returned for successful deletions.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class DeleteBucketChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return DeleteBucketResultSet(response, path)
