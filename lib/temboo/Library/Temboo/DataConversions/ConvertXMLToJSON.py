
###############################################################################
#
# ConvertXMLToJSON
# Converts data from XML format to a JSON format.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class ConvertXMLToJSON(Choreography):

    """
    Create a new instance of the ConvertXMLToJSON Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Temboo/DataConversions/ConvertXMLToJSON')


    def new_input_set(self):
        return ConvertXMLToJSONInputSet()

    def _make_result_set(self, result, path):
        return ConvertXMLToJSONResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ConvertXMLToJSONChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the ConvertXMLToJSON
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class ConvertXMLToJSONInputSet(InputSet):
        """
        Set the value of the XML input for this choreography. ((XML) The XML file that you want to convert to JSON format.)
        """
        def set_XML(self, value):
            InputSet._set_input(self, 'XML', value)


"""
A ResultSet with methods tailored to the values returned by the ConvertXMLToJSON choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class ConvertXMLToJSONResultSet(ResultSet):
        """
        Retrieve the value for the "JSON" output from this choreography execution. ((JSON) The converted data in JSON format.)
        """
        def get_JSON(self):
            return self._output.get('JSON', None)

class ConvertXMLToJSONChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ConvertXMLToJSONResultSet(response, path)
