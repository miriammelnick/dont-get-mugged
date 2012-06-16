
###############################################################################
#
# ConvertJSONToXML
# Converts data from JSON format to a XML format.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class ConvertJSONToXML(Choreography):

    """
    Create a new instance of the ConvertJSONToXML Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Temboo/DataConversions/ConvertJSONToXML')


    def new_input_set(self):
        return ConvertJSONToXMLInputSet()

    def _make_result_set(self, result, path):
        return ConvertJSONToXMLResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ConvertJSONToXMLChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the ConvertJSONToXML
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class ConvertJSONToXMLInputSet(InputSet):
        """
        Set the value of the JSON input for this choreography. ((required, json) The JSON data that you want to convert to XML.)
        """
        def set_JSON(self, value):
            InputSet._set_input(self, 'JSON', value)


"""
A ResultSet with methods tailored to the values returned by the ConvertJSONToXML choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class ConvertJSONToXMLResultSet(ResultSet):
        """
        Retrieve the value for the "XML" output from this choreography execution. ((xml) The converted data in XML format.)
        """
        def get_XML(self):
            return self._output.get('XML', None)

class ConvertJSONToXMLChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ConvertJSONToXMLResultSet(response, path)
