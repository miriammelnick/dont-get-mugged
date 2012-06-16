
###############################################################################
#
# GetXML
# Retrieves the atributes of a PDF document created from a website URL in XML format.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetXML(Choreography):

    """
    Create a new instance of the GetXML Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Joliprint/GetXML')


    def new_input_set(self):
        return GetXMLInputSet()

    def _make_result_set(self, result, path):
        return GetXMLResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetXMLChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetXML
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetXMLInputSet(InputSet):
        """
        Set the value of the URL input for this choreography. ((string) The URL of the website to convert to a PDF.)
        """
        def set_URL(self, value):
            InputSet._set_input(self, 'URL', value)


"""
A ResultSet with methods tailored to the values returned by the GetXML choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetXMLResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((XML) The response returned by the Joliprint API.)
        """
        def get_Response(self):
            return self._output.get('Response', None)
        """
        Retrieve the value for the "PDF" output from this choreography execution. ((string) The URL where you can download the printed PDF.)
        """
        def get_PDF(self):
            return self._output.get('PDF', None)

class GetXMLChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetXMLResultSet(response, path)
