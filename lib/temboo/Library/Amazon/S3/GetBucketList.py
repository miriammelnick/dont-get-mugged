
###############################################################################
#
# GetBucketList
# Retrieves a list of the items that are in a specified Amazon S3 storage bucket, and returns the list information in XML format.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetBucketList(Choreography):

    """
    Create a new instance of the GetBucketList Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Amazon/S3/GetBucketList')


    def new_input_set(self):
        return GetBucketListInputSet()

    def _make_result_set(self, result, path):
        return GetBucketListResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetBucketListChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetBucketList
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetBucketListInputSet(InputSet):
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
        Set the value of the BucketName input for this choreography. ((required, string) The name of the bucket that contains the list of objects that you want to retrieve.)
        """
        def set_BucketName(self, value):
            InputSet._set_input(self, 'BucketName', value)


"""
A ResultSet with methods tailored to the values returned by the GetBucketList choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetBucketListResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from Amazon.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetBucketListChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetBucketListResultSet(response, path)
