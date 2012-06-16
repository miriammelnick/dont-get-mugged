
###############################################################################
#
# XML
# Validates XML for basic well-formedness and allows you to check XML against a specified XSD schema file.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class XML(Choreography):

    """
    Create a new instance of the XML Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Temboo/Validation/XML')


    def new_input_set(self):
        return XMLInputSet()

    def _make_result_set(self, result, path):
        return XMLResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return XMLChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the XML
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class XMLInputSet(InputSet):
        """
        Set the value of the XMLFile input for this choreography. ((required, xml) The XML file you want to validate.)
        """
        def set_XMLFile(self, value):
            InputSet._set_input(self, 'XMLFile', value)

        """
        Set the value of the XSDFile input for this choreography. ((optional, xml) The XSD file to validate an XML file against.)
        """
        def set_XSDFile(self, value):
            InputSet._set_input(self, 'XSDFile', value)


"""
A ResultSet with methods tailored to the values returned by the XML choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class XMLResultSet(ResultSet):
        """
        Retrieve the value for the "Error" output from this choreography execution. ((string) The error description that is generated if a validation error occurs.)
        """
        def get_Error(self):
            return self._output.get('Error', None)
        """
        Retrieve the value for the "Result" output from this choreography execution. ((string) The result of the validation. Returns the string "valid" or "invalid".)
        """
        def get_Result(self):
            return self._output.get('Result', None)

class XMLChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return XMLResultSet(response, path)
