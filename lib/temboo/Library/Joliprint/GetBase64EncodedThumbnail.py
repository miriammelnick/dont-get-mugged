
###############################################################################
#
# GetBase64EncodedThumbnail
# Creates a JPEG thumbnail of a PDF document created from a website URL you specify and returns the file content as Base64 encoded data.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetBase64EncodedThumbnail(Choreography):

    """
    Create a new instance of the GetBase64EncodedThumbnail Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Joliprint/GetBase64EncodedThumbnail')


    def new_input_set(self):
        return GetBase64EncodedThumbnailInputSet()

    def _make_result_set(self, result, path):
        return GetBase64EncodedThumbnailResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetBase64EncodedThumbnailChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetBase64EncodedThumbnail
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetBase64EncodedThumbnailInputSet(InputSet):
        """
        Set the value of the URL input for this choreography. ((required, string) The URL of the website to convert to a PDF.)
        """
        def set_URL(self, value):
            InputSet._set_input(self, 'URL', value)


"""
A ResultSet with methods tailored to the values returned by the GetBase64EncodedThumbnail choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetBase64EncodedThumbnailResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response returned by the Joliprint API. The response will contain a JPEG image returned as Base64 encoded data.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetBase64EncodedThumbnailChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetBase64EncodedThumbnailResultSet(response, path)
