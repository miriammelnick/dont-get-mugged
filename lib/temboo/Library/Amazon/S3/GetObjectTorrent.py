
###############################################################################
#
# GetObjectTorrent
# Returns torrent files from an Amazon S3 bucket.t
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetObjectTorrent(Choreography):

    """
    Create a new instance of the GetObjectTorrent Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Amazon/S3/GetObjectTorrent')


    def new_input_set(self):
        return GetObjectTorrentInputSet()

    def _make_result_set(self, result, path):
        return GetObjectTorrentResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetObjectTorrentChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetObjectTorrent
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetObjectTorrentInputSet(InputSet):
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
        Set the value of the BucketName input for this choreography. ((required, string) The name of the bucket that contains the object to retrieve.)
        """
        def set_BucketName(self, value):
            InputSet._set_input(self, 'BucketName', value)

        """
        Set the value of the FileName input for this choreography. ((required, string) The name of the torrent file to retrieve.)
        """
        def set_FileName(self, value):
            InputSet._set_input(self, 'FileName', value)


"""
A ResultSet with methods tailored to the values returned by the GetObjectTorrent choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetObjectTorrentResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The retrieved file. A Bencoded dictionary as defined by the BitTorrent specification.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetObjectTorrentChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetObjectTorrentResultSet(response, path)
