
###############################################################################
#
# GetShortURL
# Retrieves the shortened URL for a PDF document created from a website URL you specify.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetShortURL(Choreography):

    """
    Create a new instance of the GetShortURL Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Joliprint/GetShortURL')


    def new_input_set(self):
        return GetShortURLInputSet()

    def _make_result_set(self, result, path):
        return GetShortURLResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetShortURLChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetShortURL
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetShortURLInputSet(InputSet):
        """
        Set the value of the URL input for this choreography. ((required, string) The URL of the website to convert to a PDF.)
        """
        def set_URL(self, value):
            InputSet._set_input(self, 'URL', value)


"""
A ResultSet with methods tailored to the values returned by the GetShortURL choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetShortURLResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((string) The response returned by the Joliprint API.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetShortURLChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetShortURLResultSet(response, path)
