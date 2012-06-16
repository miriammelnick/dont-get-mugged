
###############################################################################
#
# ConvertExcelToXML
# Converts Excel (.xls) formatted data to XML.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class ConvertExcelToXML(Choreography):

    """
    Create a new instance of the ConvertExcelToXML Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Temboo/DataConversions/ConvertExcelToXML')


    def new_input_set(self):
        return ConvertExcelToXMLInputSet()

    def _make_result_set(self, result, path):
        return ConvertExcelToXMLResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ConvertExcelToXMLChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the ConvertExcelToXML
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class ConvertExcelToXMLInputSet(InputSet):
        """
        Set the value of the ExcelFile input for this choreography. ((optional, string) The base64-encoded contents of the Excel file that you want to convert to CSV. Required unless using the VaultFile input alias (an advanced option used when running Choreos in the Temboo Designer).)
        """
        def set_ExcelFile(self, value):
            InputSet._set_input(self, 'ExcelFile', value)

        """
        Set the value of the VaultFile input for this choreography. ((optional, vault file) A path to an Excel file that has been uploaded to the vault. You can use this input alias as an alternative to the ExcelFile input variable.)
        """


"""
A ResultSet with methods tailored to the values returned by the ConvertExcelToXML choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class ConvertExcelToXMLResultSet(ResultSet):
        """
        Retrieve the value for the "XMLFile" output from this choreography execution. ((xml) The data in XML format.)
        """
        def get_XMLFile(self):
            return self._output.get('XMLFile', None)

class ConvertExcelToXMLChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ConvertExcelToXMLResultSet(response, path)
